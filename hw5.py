import multiprocessing

def halt(target_function, input_value, timeout=2):
    """
    測試目標函數是否能在指定時間內執行完成。

    :param target_function: 要執行的目標函數
    :param input_value: 傳遞給目標函數的輸入值
    :param timeout: 最大執行時間（秒），默認為2秒
    :return: 如果在指定時間內完成返回True，否則返回False
    """
    def wrapper(queue):
        try:
            target_function(input_value)
            queue.put(True)
        except Exception as e:
            print(f"函數執行時出現異常: {e}")
            queue.put(False)

    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=wrapper, args=(queue,))
    process.start()
    process.join(timeout=timeout)

    if process.is_alive():
        process.terminate()
        process.join()  # 確保進程完全終止
        return False
    else:
        return queue.get()

def f1(n):
    """簡單計算平方的函數"""
    return n * n

def f2(n):
    """執行大量循環運算的函數"""
    s = 0
    for _ in range(n):
        for _ in range(n):
            for _ in range(n):
                for _ in range(n):
                    s += 1

if __name__ == "__main__":
    print('halt(f1, 3) =', halt(f1, 3))   # 預期輸出: True
    print('halt(f2, 10) =', halt(f2, 10)) # 預期輸出: True
    print('halt(f2, 1000) =', halt(f2, 1000)) # 預期輸出: False
