# to be developed
from scipy.stats import binom
import numpy as np

class PowerStorm:
    def __init__(self, num_energy, coin_probability=0.5, damage_unit=50):
        self.num_energy = num_energy
        # self.coin_probability = coin_probability
        self.damage_unit = damage_unit
        # x軸の値（0 から n までの整数）
        self.x_coin = np.arange(0, num_energy+1)
        # 二項分布の確率質量関数 (PMF)
        self.y = binom.pmf(self.x_coin, num_energy, coin_probability)
        self.x_damage = np.arange(0, num_energy+1) * damage_unit
        self.expected_value = num_energy * coin_probability
        self.std = np.sqrt(num_energy * coin_probability * (1 - coin_probability))

    def get_damage_in_std(self, num_std=1):
        index_within_1std = np.where(np.abs(self.x_coin - self.expected_value) <= num_std * self.std)
        probability = np.sum(self.y[index_within_1std])
        damages = self.x_damage[index_within_1std]
        return damages, probability
