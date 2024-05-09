import random
import copy


class Individual:
    def __init__(self, seed):
        self.sex = None
        self.karyotype = None
        self.seed = seed

    def generate_genome(self):
        # QQ-SS-SX
        seed = self.seed
        split_seed = seed.split("-")
        qnt = int(split_seed[0])
        size = int(split_seed[1])
        sex_pool = list(split_seed[2])

        nitro_bases = ['A', 'T', 'G', 'C']

        karyotype = []
        for i in range(qnt):
            pair = []
            for j in range(2):
                chromosome = []
                for k in range(size):
                    gen = ''.join(random.choices(nitro_bases, k=3))
                    chromosome.append(gen)
                pair.append(chromosome)

            karyotype.append(pair)

        sex = ''.join(random.choices(sex_pool, k=2))

        self.karyotype = karyotype
        self.sex = sex

    def get_karyotype(self):
        return self.karyotype.copy()

    def get_sex(self):
        return self.sex.copy()


ademir = Individual("02-03-XY")
ademir.generate_genome()

kary = ademir.get_karyotype()
gamets = []

for i in range(len(kary)):
    duplicated_pair = copy.deepcopy(kary[i])+copy.deepcopy(kary[i])

    cross_1 = duplicated_pair[0][-1]
    cross_2 = duplicated_pair[1][-1]



    duplicated_pair[0][-1] = cross_2
    duplicated_pair[1][-1] = cross_1

