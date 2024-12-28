import numpy as np
import time

def f(x, y, z):
    """被積分函數: 3x^2 + y^2 + 2z^2"""
    return 3*x**2 + y**2 + 2*z**2

def riemann_integral(n):
    """
    使用黎曼積分計算
    Args:
        n: 每個維度的分割數量
    """
    dx = 1.0 / n
    dy = 1.0 / n
    dz = 1.0 / n
    
    total = 0.0
    for i in range(n):
        x = (i + 0.5) * dx  # 使用中點法則
        for j in range(n):
            y = (j + 0.5) * dy
            for k in range(n):
                z = (k + 0.5) * dz
                total += f(x, y, z) * dx * dy * dz
    
    return total

def monte_carlo_integral(n):
    """
    使用蒙地卡羅法計算
    Args:
        n: 隨機採樣點的數量
    """
    # 在單位立方體中隨機生成點
    x = np.random.uniform(0, 1, n)
    y = np.random.uniform(0, 1, n)
    z = np.random.uniform(0, 1, n)
    
    # 計算函數值的平均
    values = f(x, y, z)
    result = np.mean(values)
    
    # 體積為1的立方體，所以不需要乘以體積
    return result

def calculate_theoretical_value():
    """計算積分的理論值"""
    # ∫∫∫(3x^2 + y^2 + 2z^2)dxdydz from 0 to 1
    # = ∫∫(x^3 + xy^2 + 2xz^2)|_0^1 dydz
    # = ∫∫(1 + y^2 + 2z^2)dydz
    # = ∫(y + y^3/3 + 2yz^2)|_0^1 dz
    # = ∫(1 + 1/3 + 2z^2)dz
    # = [z + z/3 + 2z^3/3]|_0^1
    # = (1 + 1/3 + 2/3) = 2
    return 2.0

def compare_methods():
    """比較不同方法的結果和性能"""
    theoretical = calculate_theoretical_value()
    print(f"理論值: {theoretical}\n")
    
    # 測試不同的n值
    riemann_ns = [10, 20, 50, 100]
    monte_carlo_ns = [1000, 10000, 100000, 1000000]
    
    print("黎曼積分結果:")
    print("n\t結果\t\t誤差\t\t時間(秒)")
    print("-" * 50)
    for n in riemann_ns:
        start_time = time.time()
        result = riemann_integral(n)
        end_time = time.time()
        error = abs(result - theoretical)
        print(f"{n}\t{result:.6f}\t{error:.6f}\t{end_time-start_time:.4f}")
    
    print("\n蒙地卡羅法結果:")
    print("n\t\t結果\t\t誤差\t\t時間(秒)")
    print("-" * 50)
    for n in monte_carlo_ns:
        start_time = time.time()
        result = monte_carlo_integral(n)
        end_time = time.time()
        error = abs(result - theoretical)
        print(f"{n}\t{result:.6f}\t{error:.6f}\t{end_time-start_time:.4f}")

if __name__ == "__main__":
    # 設置隨機種子以獲得可重複的結果
    np.random.seed(42)
    
    # 運行比較
    compare_methods()
