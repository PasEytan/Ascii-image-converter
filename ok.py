from player import playvid
import multiprocessing

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    res = pool.apply_async(playvid())