import random

gen_str = '0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'
gen_str_bin = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'a':'1010',
    'b':'1011',
    'c':'1100',
    'd':'1101',
    'e':'1110',
    'f':'1111'
    }

def replace_lst(lst, dct) -> list:
    stub_lst = list(lst)
    for i, e in enumerate(lst):
        if e in dct:
            stub_lst[i] = dct[e]
    return stub_lst

class Brain:
    def __init__(self, genome, n_gen):
        self.genome = ''
        if (genome == None) and (n_gen != 0):
            e = 0
            while e < n_gen:
                gen = ''
                i = 0
                while i < 8:
                    gen += random.choice(gen_str)
                    i += 1
                self.genome += gen
                self.genome += ' '
                e += 1
        elif (n_gen == 0) and (genome != None):
            self.genome = genome
    
    def mutation(self, genome):
        gen_lib = []
        gen_lib_p = ''
        gen_split = genome.split(' ')
        if gen_split.count('') > 0:
            gen_split.remove('')
        for i in range(len(gen_split)):
            gen_lib += [gen_split[i][index : index + 1] for index in range(0, len(gen_split[i]), 1)]
        for e in range(gen_lib.count(' ')):
            gen_lib.remove(' ')
        gen_lib[random.randint(0, len(gen_lib) - 1)] = random.choice(gen_str)
        i = 0
        for i, e in enumerate(gen_lib):
            if i % 8 == 0 and i != 0:
                gen_lib_p += ' '
            gen_lib_p += e
    
    def get_info(self):
        genome = self.genome
        gen_lib = []
        gen_lib_p = ''
        gen_split = genome.split(' ')
        if gen_split.count('') > 0:
            gen_split.remove('')
        gen_lib_spl = []
        for i in range(len(gen_split)):
            gen_lib += [gen_split[i][index : index + 1] for index in range(0, len(gen_split[i]), 1)]
        for e in range(gen_lib.count(' ')):
            gen_lib.remove(' ')
        
        gen_lib = [gen_str_bin[i] if i in gen_str_bin else i for i in gen_lib]
        
        i = 0
        for i, e in enumerate(gen_lib):
            if i % 8 == 0 and i != 0:
                gen_lib_p += ' '
            gen_lib_p += e
        for i in range(len(gen_lib_p)):
            gen_lib_spl += [gen_lib_p[i][index : index + 1] for index in range(0, len(gen_lib_p[i]), 1)]
        for e in range(gen_lib_spl.count(' ')):
            gen_lib_spl.remove(' ')

        info = []
        z = 0
        for j in range(len(gen_split)):
            inn = str(gen_lib_spl[0])
            inn_id = ''
            sn = str(gen_lib_spl[8])
            sn_id = ''
            weight = ''
            for i in range(7):
                inn_id += str(gen_lib_spl[i+1+z])
                sn_id += str(gen_lib_spl[i+7+z])
            for i in range(16):
                weight += str(gen_lib_spl[i+15+z])
            z += 32

            info.append([int('0b' + str(inn), 2), int('0b' + str(inn_id), 2), int('0b' + str(sn), 2), int('0b' + str(sn_id), 2), int('0b' + str(weight), 2)])
        return info
