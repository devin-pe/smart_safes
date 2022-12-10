from vault import *

def record_success(pt_path, iters):
    start('pass', pt_path)
    start_time = time.time()
    for _ in range(iters):
        # Decrypt and actaully assign to variables to mimic regular control flow
        flag, pt, obj = decrypt_load('pass') 
    avg_duration = (time.time()-start_time)/iters
    print(f'Average time taken to decrypt {pt_path} successfully: {avg_duration}')


def record(iters=500):
    """Runs and  all trials"""

    
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
    print(f'Maximum unsuccessful decryption time: {max_duration}')
    print(f'Minimum unsuccessful decryption time: {min_duration}')

record()