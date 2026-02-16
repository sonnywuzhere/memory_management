import memory as m

def main():
    # test1 = m.release_memory(
    #     {"start_address": 16, "end_address": 23, "segment_size": 8, "process_id": 13},
    #     [
    #         {"start_address": 0, "end_address": 7, "segment_size": 8, "process_id": 12},
    #         {"start_address": 8, "end_address": 15, "segment_size": 8, "process_id": 0},
    #         {"start_address": 16, "end_address": 23, "segment_size": 8, "process_id": 13},
    #         {"start_address": 24, "end_address": 27, "segment_size": 4, "process_id": 0},
    #         {"start_address": 28, "end_address": 29, "segment_size": 2, "process_id": 11}
    #     ]
    # )

    # test2 = m.best_fit_allocate(
    #     10,
    #     [{"start_address": 0, "end_address": 1023, "segment_size": 1024, "process_id": 0}],
    #     32
    # )
    # print(test2)

    memory_block2 = [
        {"start_address": 0, "end_address": 19, "segment_size": 20, "process_id": 10},
        {"start_address": 20, "end_address": 39, "segment_size": 20, "process_id": 0},
        {"start_address": 40, "end_address": 49, "segment_size": 10, "process_id": 20},
        {"start_address": 50, "end_address": 1023, "segment_size": 974, "process_id": 0},        
    ]

    memory_block3 = [
        {"start_address": 0, "end_address": 19, "segment_size": 20, "process_id": 10},
        {"start_address": 20, "end_address": 39, "segment_size": 20, "process_id": 0},
        {"start_address": 40, "end_address": 49, "segment_size": 10, "process_id": 20},
        {"start_address": 50, "end_address": 1023, "segment_size": 974, "process_id": 30},   
    ]

    memory_block4 = [
        {"start_address": 0, "end_address": 19, "segment_size": 20, "process_id": 10},
        {"start_address": 20, "end_address": 39, "segment_size": 20, "process_id": 0},
        {"start_address": 40, "end_address": 54, "segment_size": 15, "process_id": 0},
        {"start_address": 55, "end_address": 1023, "segment_size": 969, "process_id": 30},   
    ]

    test2 = m.best_fit_allocate(20, memory_block3, 40)
    test3 = m.best_fit_allocate(30, memory_block4, 40)
    print(test2)
    print(test3)
    best_fit_allocate_mb4 = [
        {"start_address": 0, "end_address": 19, "segment_size": 20, "process_id": 0},
        {"start_address": 20, "end_address": 39, "segment_size": 20, "process_id": 20},
        {"start_address": 40, "end_address": 54, "segment_size": 15, "process_id": 0},
        {"start_address": 55, "end_address": 1023, "segment_size": 969, "process_id": 30},   
    ]

    print(m.best_fit_allocate(10, best_fit_allocate_mb4, 40))

    worst_fit_allocate_mb1 = [
        {"start_address": 0, "end_address": 1023, "segment_size": 1024, "process_id": 0}
    ]

    worst_fit_allocate_mb4 = [
        {"start_address": 0, "end_address": 19, "segment_size": 20, "process_id": 0},
        {"start_address": 20, "end_address": 39, "segment_size": 20, "process_id": 20},
        {"start_address": 40, "end_address": 54, "segment_size": 15, "process_id": 30},
        {"start_address": 55, "end_address": 1023, "segment_size": 969, "process_id": 0}, 
    ]

    # print(m.worst_fit_allocate(10, worst_fit_allocate_mb4, 40))

    next_fit_memory_mb1 = [
            {"start_address": 0, "end_address": 1023, "segment_size": 1024, "process_id": 0}
    ]

    next_fit_memory_mb4 = [
        {"start_address": 0, "end_address": 19, "segment_size": 20, "process_id": 0},
        {"start_address": 20, "end_address": 39, "segment_size": 20, "process_id": 20},
        {"start_address": 40, "end_address": 54, "segment_size": 15, "process_id": 0},
        {"start_address": 55, "end_address": 74, "segment_size": 20, "process_id": 30},  
        {"start_address": 75, "end_address": 1023, "segment_size": 949, "process_id": 0},    
    ]
    # print(m.next_fit_allocate(30, next_fit_memory_mb4, 40, 2))

    release_memory_mb1 = [
        {"start_address": 0, "end_address": 7, "segment_size": 8, "process_id": 12},
        {"start_address": 8, "end_address": 15, "segment_size": 8, "process_id": 0},
        {"start_address": 16, "end_address": 23, "segment_size": 8, "process_id": 13},  
        {"start_address": 24, "end_address": 27, "segment_size": 4, "process_id": 0},
        {"start_address": 28, "end_address": 29, "segment_size": 2, "process_id": 11},        
    ]

    # print(m.release_memory({"start_address": 16, "end_address": 23, "segment_size": 8, "process_id": 13}, release_memory_mb1))


main()