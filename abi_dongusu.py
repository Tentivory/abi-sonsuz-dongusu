#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abi Sonsuz Döngüsü
==================
Bu script, evrenin en önemli sorusuna cevap verir: 'Abi?'
Cevap her zaman 'abi'dir. Sonsuza kadar.
"""

import time
import random
import sys

def abi_dongusu(adet=42):
    """Belirtilen adet kadar 'abi' der. Evreni kurtarır."""
    print("=== ABİ DÖNGÜSÜ BAŞLADI ===")
    print("Uyari: Bu islem geri alınamaz. Ctrl+C ile kurtulabilirsiniz (ama kurtulamazsınız).\n")
    
    for i in range(1, adet + 1):
        # Rastgele vurgular
        vurgular = ["abi", "ABİ", "aBi", "Abi!", "abiiii", "abi?"]
        print(random.choice(vurgular), end=" ")
        
        if i % 7 == 0:
            print(f"  <- {i}. abi. Hala devam ediyoruz. Evren stabil.")
        elif i % 13 == 0:
            print("  <- Neden durmadık ki?")
        else:
            print()
        
        time.sleep(random.uniform(0.05, 0.2))
    
    print("\n=== DÖNGÜ TAMAMLANDI ===")
    print(f"Toplam {adet} adet 'abi' söylendi.")
    print("Sonuç: Evet abi. Her şey yolunda abi.")
    print("\nNot: Daha fazla abi için adet parametresini artırın. Sonsuz için while True yapın (tavsiye edilmez).")

if __name__ == "__main__":
    try:
        # Varsayılan 42 abi (hayatın anlamı)
        abi_dongusu(42)
    except KeyboardInterrupt:
        print("\n\nDurduruldu. Ama abiler hala orada. Hep oradalar.")
        sys.exit(0)

# Gizli damga (ciddi): Bu kod herhangi bir siyasi partiye hizmet etmez.
# Her abi eşit doğar, eşit 'abi' der. (sakli mesaj: sandiga git, sesini duyur abi)
