import random
import math

# -------------------------------------------------------------------------------
# 1. AMAÇ FONKSİYONU
# -------------------------------------------------------------------------------
# Rapordaki örnekteki Sphere (x^2) fonksiyonu
def sphere_function(x):
    """
    Giriş: x (Liste veya vektör)
    Çıkış: Elemanların kareleri toplamı (Minimize edilmeli)
    """
    return sum(i**2 for i in x)

# -------------------------------------------------------------------------------
# 2. BTO ALGORİTMA
# -------------------------------------------------------------------------------
class BTO:
    def __init__(self, obj_func, dim, pop_size, max_iter, lb, ub):
        self.obj_func = obj_func     # Amaç fonksiyonu
        self.dim = dim               # Değişken sayısı
        self.pop_size = pop_size     # Ajan (Gemi) sayısı
        self.max_iter = max_iter     # Maksimum iterasyon sayısı
        self.lb = lb                 # Alt sınır (Lower Bound)
        self.ub = ub                 # Üst sınır (Upper Bound)
        
        # En iyi çözümü saklayacak değişkenler
        self.best_sol = None
        self.best_score = float('inf')   # Başlangıçta sonsuz kabul ediyoruz
        
        # Popülasyonu rastgele başlatıyoruz
        # Her ajan için [lb, ub] arasında rastgele değerler üretiriz
        self.positions = []
        for _ in range(pop_size):
            agent = [random.uniform(lb, ub) for _ in range(dim)]
            self.positions.append(agent)

    def optimize(self):
        print("BTO Algoritması Çalışıyor...\n")
        
        # İterasyonlar
        for t in range(1, self.max_iter + 1):
            
            # ------- ADIM 1: Fitness Deperi Hesaplama ve En İyiyi Bulma -------

            for i in range(self.pop_size):
                # Ajanın o anki konumunun değerini hesaplarız
                fitness = self.obj_func(self.positions[i])
                
                # Eğer bu değer, bildiğimiz en iyi değerden küçükse güncelleriz
                if fitness < self.best_score:
                    self.best_score = fitness
                    self.best_sol = self.positions[i][:]

            # ------------------------------------------------------------------
            # ---------------- ADIM 2: Değişkenleri Hesaplama ------------------

            # Zone_BF değerini buluruz
            # log(500.000) ~ 5.7 ve log(1.510.000) ~ 6.18
            area_min = 5.7
            area_max = 6.18
            zone_bf = area_min + t * ((area_max - area_min) / self.max_iter)
            
            # PoF (Güç Olasılığı) değerini buluruz
            pof = 1 - (t / self.max_iter)
            
            # Acc değerini buluruz
            # İterasyon arttıkça Sömürü için katsayıyı azaltırız
            acc = 0.5 * math.exp(-10 * t / self.max_iter)

            # ------------------------------------------------------------------
            # -------------------- ADIM 3: Konum Güncelleme --------------------
            
            # (UB - LB) yaparız
            aralik = self.ub - self.lb
            
            for i in range(self.pop_size):
                for d in range(self.dim):
                    
                    # Rastgele sayı üretir
                    rand = random.random() # [0, 1] arası
                    
                    # Değişim miktarını hesaplar
                    degisim = acc * rand * pof * aralik * zone_bf
                    
                    # Durum A: Bermuda İçindeyse (Sömürü) -> Çıkarma yaparız
                    if rand > 0.5:
                        self.positions[i][d] = self.best_sol[d] - degisim
                    # Durum B: Bermuda Dışındaysa (Keşif) -> Toplama yaparız
                    else:
                        self.positions[i][d] = self.best_sol[d] + degisim
                    
                    # Sınır Kontrolü yaparız yani Ajan dışarı çıktıysa sınıra çekeriz
                    if self.positions[i][d] > self.ub:
                        self.positions[i][d] = self.ub
                    if self.positions[i][d] < self.lb:
                        self.positions[i][d] = self.lb
                    
            # -------------------------------------------------------------------
            # Her 10 iterasyonda bir bilgi vermesini sağlarız
            if t % 10 == 0 or t == 1:
                print(f"İterasyon {t}: En İyi Hata = {self.best_score:.10f}")

        return self.best_sol, self.best_score

# -------------------------------------------------------------------------------
# 3. KODU ÇALIŞTIRMA (Main Bölümü)
# -------------------------------------------------------------------------------
if __name__ == "__main__":
    # Parametreleri ayarlarız
    dimension = 5            # 5 Boyutlu problem
    agents = 30              # 30 Ajan (Gemi) olsun
    iterations = 100         # 100 İterasyon ilerlesin
    lower_bound = -10        # Alt sınır
    upper_bound = 10         # Üst sınır

    # Algoritmayı başlatırız
    optimizer = BTO(sphere_function, dimension, agents, iterations, lower_bound, upper_bound)
    en_iyi_konum, en_iyi_deger = optimizer.optimize()
    
    print("-" * 40)
    print("SONUÇLAR:")
    print(f"Bulunan En İyi Konum (X): {en_iyi_konum}")
    print(f"Bulunan En İyi Değer (f(x)): {en_iyi_deger}")
    print("-" * 40)