from pynq import DefaultHierarchy, DefaultIP, allocate
import numpy as np
import struct

class AxiStreamHandler():

    def __init__(self, overlay, model_specs, X_test, y_test):
        self.firmware_name = overlay
        self.model_specs = model_specs
        self.batch_size = self.model_specs["batch_size"]
        self.X_test = X_test
        self.samples_len = len(self.X_test)
        self.overlay = overlay
        self.fill = False
        self.batches = []
        self.last_batch_size = 0
        self.n_input = self.model_specs['n_input']
        self.n_output = self.model_specs['n_output']
        self.benchcore = self.model_specs['benchcore']
        if self.benchcore == True:
            self.n_output = self.n_output + 1
        self.input_shape  = (self.batch_size, self.n_input)
        self.output_shape = (self.batch_size, self.n_output)
        self.datatype = None
        self.scale = None
        self.__initialize_datatype()
        self.__init_channels()
        if self.model_specs["data_type"][:3] == "fps":
            self.__initialize_fixedpoint()
        self.__prepare_data()
        
    def __bin_to_float16(self, binary_str):
        binary_bytes = int(binary_str, 2).to_bytes(2, byteorder='big')
        float_val = struct.unpack('>e', binary_bytes)[0]
        return float_val

    def __bin_to_float32(self, binary_str):
        byte_str = int(binary_str, 2).to_bytes(4, byteorder='big')
        float_value = struct.unpack('>f', byte_str)[0]
        return float_value

    def __random_pad(self, vec, pad_width, *_, **__):
        vec[:pad_width[0]] = np.random.uniform(0, 1, size=pad_width[0])
        vec[vec.size-pad_width[1]:] = np.random.uniform(0,1, size=pad_width[1])

    def __prepare_data(self):
        n_batches = 0
        self.fill = False
        if (self.samples_len/self.batch_size % 2 != 0):
            n_batches = int(self.samples_len/self.batch_size) + 1
            self.fill = True
        else:
            n_batches = int(self.samples_len/self.batch_size)

        self.last_batch_size = 0
        for i in range(0, n_batches):
            new_batch = self.X_test[i*self.batch_size:(i+1)*self.batch_size]
            if (len(new_batch) < self.batch_size):
                self.last_batch_size = len(new_batch)
                new_batch = np.pad(new_batch,  [(0, self.batch_size-len(new_batch)), (0,0)], mode=self.__random_pad)

            if self.datatype == "np.fps16f6":
                new_batch = np.vectorize(self.__float_to_fixed)(new_batch)
            self.batches.append(new_batch)

    def __init_channels(self):
        self.sendchannel = self.overlay.axi_dma_0.sendchannel
        self.recvchannel = self.overlay.axi_dma_0.recvchannel

    def __initialize_fixedpoint(self):
        self.total_bits = self.model_specs['register_size']  # Total number of bits
        fractional_bits = int(self.model_specs['data_type'][6:7])  # Number of fractional bits
        self.scale = 2 ** fractional_bits

    def __float_to_fixed(self, number):
        return int(number * self.scale)

    def __fixed_to_float(self, fixed_number):
        if fixed_number >= (1 << (self.total_bits - 1)):
            fixed_number -= (1 << self.total_bits)
        return fixed_number / self.scale

    def __initialize_datatype(self):
        if (self.model_specs["data_type"] == "float16"):
            self.datatype = "np.float16"
        elif (self.model_specs["data_type"] == "float32"):
            self.datatype = "np.float32"
        elif (self.model_specs["data_type"] == "fps16f6"):
            self.datatype = "np.fps16f6"
        else:
            raise Exception("Data type not supported yet")

    def __get_dtype(self):
        if (self.model_specs["data_type"] == "float16"):
            return np.float16, np.uint16
        elif (self.model_specs["data_type"] == "float32"):
            return np.float32, np.uint32
        elif (self.model_specs["data_type"] == "fps16f6"):
            return np.int16, np.int16
        else:
            raise Exception("Data type not supported yet")

    def __parse_prediction(self, outputs):
        hw_classifications = []
        for outcome in outputs:
            for out in outcome:
                
                if self.datatype == "np.fps16f6":
                    probs = []
                    for i in range(0, self.n_output):
                        prob = self.__fixed_to_float(out[i])
                        probs.append(prob)
                else:
                    probs = []
                    if self.model_specs['register_size'] == 16:
                        for i in range(0, self.n_output):
                            if self.benchcore == True and i == self.n_output - 1:
                                probs.append(out[i])
                            else:
                                binary_str = bin(out[i])[2:]
                                prob_float = self.__bin_to_float16(binary_str)
                                probs.append(prob_float)

                    elif self.model_specs['register_size'] == 32:
                        for i in range(0, self.n_output):
                            if self.benchcore == True and i == self.n_output - 1:
                                probs.append(out[i])
                            else:
                                binary_str = bin(out[i])[2:].zfill(32)
                                prob_float = self.__bin_to_float32(binary_str)
                                probs.append(prob_float)
                    
                classification = np.argmax(probs[:-1])
                hw_classifications.append(int(classification))

        return hw_classifications

    def predict(self):
        outputs = []
        data_type_input, data_type_output = self.__get_dtype()

        input_buffer = allocate(shape=self.input_shape, dtype=data_type_input)

        for i in range(0, len(self.batches)):
            input_buffer[:]=self.batches[i]
            output_buffer = allocate(shape=self.output_shape, dtype=data_type_output)
            self.sendchannel.transfer(input_buffer)
            self.recvchannel.transfer(output_buffer)
            self.sendchannel.wait()
            self.recvchannel.wait()
            if len(self.batches) == 1:
                outputs.append(output_buffer)
                return
            if self.fill == True and i == len(self.batches) - 1:
                outputs.append(output_buffer[0:self.last_batch_size])
            else:
                outputs.append(output_buffer)

        return self.__parse_prediction(outputs)

