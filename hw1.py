# 預先計算並存儲 2^n 的結果直到 n=1000
POWER_TABLE = [2**n for n in range(1001)]  # 包含 n=1000

def power2n_d(n):
    """
    使用查表法快速計算 2^n
    
    Args:
        n: 指數
    Returns:
        2^n 的結果
    """
    if n < 0:
        return 0
    if n > 1000:
        return 2**n  # 超出查表範圍時使用直接計算
    return POWER_TABLE[n]

# 測試代碼
def test_power2n_d():
    """
    測試優化後的 power2n_d 函數
    """
    test_cases = [0, 1, 2, 3, 4, 5, 10, 20, 30, 100, 1000]
    
    print("測試 power2n_d 函數：")
    for n in test_cases:
        result = power2n_d(n)
        print(f"2^{n} = {result}")
        
        # 驗證結果正確性
        assert result == 2**n, f"錯誤：2^{n} 計算結果不正確"

if __name__ == "__main__":
    import time
    
    # 性能測試
    print("進行性能測試...\n")
    
    # 測試優化後的函數
    start_time = time.time()
    for i in range(1000):
        power2n_d(100)
    optimized_time = time.time() - start_time
    
    # 測試原始計算
    start_time = time.time()
    for i in range(1000):
        2**100
    original_time = time.time() - start_time
    
    print(f"優化後函數執行1000次耗時：{optimized_time:.6f} 秒")
    print(f"原始計算執行1000次耗時：{original_time:.6f} 秒")
    print(f"性能提升：{original_time/optimized_time:.2f}倍")
    
    # 運行功能測試
    test_power2n_d()
