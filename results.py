from vault import *

def record_success(pt_path, iters):
    start('pass', pt_path)
    start_time = time.time()
    for _ in range(iters):
        # Decrypt and actaully assign to variables to mimic regular control flow
        flag, pt, obj = decrypt_load('pass') 
    avg_duration = (time.time()-start_time)/iters
    # short: 0.054322242736816406  medium: 0.055107023239135744  long: 0.05461845254898071
    print(f'Average time taken to decrypt {pt_path} successfully: {avg_duration}')
    # medium2: 0.452160231590271

def record(iters=500):
    """Runs and  all trials"""

    # Run the sucessful
    short_path = 'plaintexts/short.txt'
    medium_path = 'plaintexts/medium.txt'
    long_path = 'plaintexts/long.txt'
    #record_success(short_path, iters)
    record_success(medium_path, iters)
    #record_success(long_path, iters)

    start_time = time.time()
    max_duration = 0; min_duration = np.Inf
    for _ in range(iters):
        iter_start_time = time.time()
        decrypt_load('incorrect')
        iter_duration = time.time()-iter_start_time
        max_duration = max(max_duration, iter_duration)
        if iter_duration > 0.1:
            min_duration = min(min_duration, iter_duration)
    avg_duration = (time.time()-start_time)/iters
    print(f'Average time taken to decrypt unsuccessfully: {avg_duration}')
    # 0.6694933376312255 - 0.46015363311767576
    print(f'Maximum unsuccessful decryption time: {max_duration}')
    # 1.0979440212249756 
    print(f'Minimum unsuccessful decryption time: {min_duration}')
    # 0.05288267135620117 - 0.4163169860839844

record()