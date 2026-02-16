def setup_memory_block(start_address,end_address,segment_size,process_id):
   memory_block = {
      "start_address": start_address,
      "end_address": end_address,
      "segment_size": segment_size,
      "process_id": process_id
    }
   return(memory_block)

# method given size of memory requested, memory map (list of MEMORY_BLOCK dictionairies), and requesting process id 
def best_fit_allocate(request_size, memory_map,process_id):
   found = False 
   candidate_blocks = []

   # finds candidate memory blocks that can be allocated 
   for block in memory_map: 
      # if the process id is 0, then it is a free block 
      # check if segment is larger than request size 
      if block["process_id"] == 0 and block["segment_size"] >= request_size and not found:
         found = True
         candidate_blocks.append(block)
    
   # if a candidate isn't found, return NULLBLOCK
   if not found: 
      return setup_memory_block(0, 0, 0, 0)
   
   print("Candidate blocks!")
   for block in candidate_blocks:
      print(block)
   print()

   # chooses the one whose size is closest to requested size 
   # put the first block in the chosen block as a placeholder/reference point 
   chosen_block = candidate_blocks[0]
   print("Chosen block")
   print(chosen_block)
   print()
   closet_size = chosen_block["segment_size"] - request_size
   for block in candidate_blocks:
      # if the segment size is the same,
      # chosen block's process id is updated to be process id 
      # return this block 
      if chosen_block["segment_size"] == request_size:
         chosen_block["process_id"] = process_id
         return chosen_block
      # segment size is different than request size 
      else:
         # see if block segment size difference is smaller than current closet size 
         if (chosen_block["segment_size"]) < closet_size: 
            chosen_block = block 
            closet_size = chosen_block["segment_size"] - request_size

    # at this point, you have a memory block available for the request (chosen_block)
    # the segment size is bigger than the request, so it needs to be split

#    new_memory_map = []
#    # loop through memory map to match where chosen_block is to split in that location 
#    for block in memory_map:
#       if chosen_block == block:
#          print("we found the spot!")
#          # split the block here before appending
#             # create a new block to append to memory map  
#             # second piece becomes free block in memory map 
#          free_memory_block = setup_memory_block(chosen_block["start_address"] + request_size,
#                                                     chosen_block["end_address"],
#                                                     chosen_block["end_address"] - (chosen_block["start_address"] + request_size) + 1, 
#                                                     0)
#             # allocate the first piece 
#             # start_address remains the same 
#             # end_address is start_address + request_size - 1 
#          chosen_block["end_address"] = chosen_block["start_address"] + request_size - 1
#             # segment_size is the request_size 
#          chosen_block["segment_size"] = request_size
#             # process_id is the process_id
#          chosen_block["process_id"] = process_id
#          new_memory_map.append("chosen block ->")
#          new_memory_map.append(chosen_block)
#          new_memory_map.append("free memory ->")
#          new_memory_map.append(free_memory_block)
#       else:
#         new_memory_map.append(block)
    

   
#    print("here is the new memory map:")
#    for block in new_memory_map:
#       print(block)
#    memory_map = new_memory_map

   # if free_block is exactly same size as requested size
   if chosen_block["segment_size"] == request_size:
      # free_block process_id is updated to be the process_id 
      chosen_block["process_id"] = process_id
      # memory map is updated 
      for block in memory_map:
         if block == chosen_block:
            block = chosen_block
      # return free block 
      return chosen_block
   elif chosen_block["segment_size"] > request_size:
   # if free_block is larger than requested size 
   # block split into two pieces 
   # first piece allocated to the requested process 

   # second piece becomes a free block in memory map 
      second_memory_piece = setup_memory_block(chosen_block["start_address"] + request_size, chosen_block["end_address"], \
                                            chosen_block["end_address"] - (chosen_block["start_address"] + request_size) + 1, 0)
    # the first piece allocated to requested process 
      chosen_block["end_address"] = chosen_block["start_address"] + request_size - 1
      chosen_block["process_id"] = process_id
      chosen_block["segment_size"] = request_size

   # update memory_map 
   # these two pieces are added to memory map (in same place as block from before)
      new_block_index = memory_map.index(chosen_block)
      memory_map[new_block_index] = chosen_block
      memory_map.insert(new_block_index + 1, second_memory_piece)

    # return memory block
   return chosen_block
   
        

# method given size of memory requested, memory map (a list of MEMORY_BLOCK dictionaries), and requesting process id
def first_fit_allocate(request_size, memory_map, process_id):
   found = False
   candidate_block = setup_memory_block(0,0,0,0)
   # loops through blocks in memory map 
   for block in memory_map:
      # finds first lowest starting address free memory block 
      # at least as large as requested size
      # 0 as a process id indicates the process is a free block 
      if block["segment_size"] >= request_size and block["process_id"] == 0 and not found:
         # block has been found 
         found = True
         # update candidate block to be the found block 
         candidate_block = block
   # if the block wasn't found 
   if not found:
      # return NULLBLOCK 
      return setup_memory_block(0,0,0,0)
   # if the free block's size is exactly the same as the requested size
   elif candidate_block["segment_size"] == request_size: 
    # update process id to allocate it to the new process id
    candidate_block["process_id"] = process_id
    # return this memory block 
    return candidate_block
   # if the free block's size is larger than the requested size 
   else:
    # split free block into two pieces 
    # the second piece becomes a free block in memory map 
    memory_map.append(setup_memory_block(candidate_block["start_address"] + request_size, candidate_block["end_address"], \
                                            candidate_block["end_address"] - (candidate_block["start_address"] + request_size) + 1, 0)) 
    # the first piece allocated 
    candidate_block["end_address"] = candidate_block["start_address"] + request_size - 1
    candidate_block["process_id"] = process_id
    candidate_block["segment_size"] = request_size
    return candidate_block

# finds candidate memory block that can be allocated 
# and chooses the largest among the blocks 
def worst_fit_allocate(request_size, memory_map,process_id):
   found = False 
   candidate_blocks = []
   # find candidate memory block (process_id = 0) and segment_size >= request size 
   for block in memory_map: 
      if block["segment_size"] >= request_size and block["process_id"] == 0 and not found:
         found = True 
         candidate_blocks.append(block)

   # if no candidate memory block is found, return NULL BLOCK 
   if not found: 
      return setup_memory_block(0, 0, 0, 0)
   
   # at least one block is in candidate blocks 

   # chooses largest segment_size among the blocks 
   # set first in candidate blocks as reference point 
   largest_segment_block = candidate_blocks[0]
   for block in candidate_blocks:
      # if segment_size is larger than what is in largest_segment_block 
      # then update to be that block
      if block["segment_size"] > largest_segment_block["segment_size"]:
         largest_segment_block = block 

   # if free_block is exactly same size as requested size
   if largest_segment_block["segment_size"] == request_size:
      # free_block process_id is updated to be the process_id 
      largest_segment_block["process_id"] = process_id
      # memory map is updated 
      for block in memory_map:
         if block == largest_segment_block:
            block = largest_segment_block
      # return free block 
      return largest_segment_block
   elif largest_segment_block["segment_size"] > request_size:
   # if free_block is larger than requested size 
   # block split into two pieces 
   # first piece allocated to the requested process 

   # second piece becomes a free block in memory map 
      second_memory_piece = setup_memory_block(largest_segment_block["start_address"] + request_size, largest_segment_block["end_address"], \
                                            largest_segment_block["end_address"] - (largest_segment_block["start_address"] + request_size) + 1, 0)
    # the first piece allocated to requested process 
      largest_segment_block["end_address"] = largest_segment_block["start_address"] + request_size - 1
      largest_segment_block["process_id"] = process_id
      largest_segment_block["segment_size"] = request_size

   # update memory_map 
   # these two pieces are added to memory map (in same place as block from before)
      new_block_index = memory_map.index(largest_segment_block)
      memory_map[new_block_index] = largest_segment_block
      memory_map.insert(new_block_index + 1, second_memory_piece)

   # returns memory block 
   return largest_segment_block
      
# finds first (lowest starting address) free memory block 
# greater than or equal to the previously allocated block address 
# whose size is at least as the requested size 
def next_fit_allocate(request_size, memory_map, process_id, last_address):
    found = False 
    found_block = 0
    # search through memory map 
    # check process_id and segment_size
    for block in memory_map:
       if block["process_id"] == 0 and block["segment_size"] >= request_size and not found:
          found = True 
          found_block = block

    # if no free block is found (not available or not big enough)
    if not found: 
    # a NULL BLOCK is returned 
        return setup_memory_block(0, 0, 0, 0) 

    # beyond this, the block has been found

    # if the free block found is exactly the same size as requested size 
    if found_block["segment_size"] == request_size:
    # the method updates process id to allocate it 
    # updates memory map 
        for block in memory_map:
           if block == found_block:
              found_block["process_id"] = process_id
    # returns memory block 
        return found_block

    # if free block found is larger than requested size 
    if found_block["segment_size"] > request_size:
   # if free_block is larger than requested size 
   # block split into two pieces 
   # first piece allocated to the requested process 

   # second piece becomes a free block in memory map 
      second_memory_piece = setup_memory_block(found_block["start_address"] + request_size, found_block["end_address"], \
                                            found_block["end_address"] - (found_block["start_address"] + request_size) + 1, 0)
    # the first piece allocated to requested process 
      found_block["end_address"] = found_block["start_address"] + request_size - 1
      found_block["process_id"] = process_id
      found_block["segment_size"] = request_size

   # update memory_map 
   # these two pieces are added to memory map (in same place as block from before)
      new_block_index = memory_map.index(found_block)
      memory_map[new_block_index] = found_block
      memory_map.insert(new_block_index + 1, second_memory_piece)
      
      print("Memory map")
      for block in memory_map:
         print(block)
      print()
      return found_block 
    
# releases a memory block, modifying the memory map passed in 
# returns the modified memory map
def release_memory(freed_block, memory_map): 
   # marks released block of memory as free (process_id = 0)
   freed_block_index = 0
   block_before_free_block = 0
   block_after_free_block = 0
   for block in memory_map:
      if block == freed_block:
         block["process_id"] = 0
         freed_block_index = memory_map.index(block)
   block_before_free_block = memory_map[freed_block_index - 1]
   block_after_free_block = memory_map[freed_block_index + 1]

   # both block before and block after free block are free 
   if block_before_free_block["process_id"] == 0 and block_after_free_block["process_id"] == 0:
   # the block before the free block's end_address becomes the address of the block after the free block
      block_before_free_block["end_address"] = block_after_free_block["end_address"]
      block_before_free_block["segment_size"] += block_after_free_block["segment_size"] + freed_block["segment_size"]
      # remove freed_block 
      memory_map.pop(freed_block_index)
      # remove block after free block 
      memory_map.remove(block_after_free_block)
   # if just the block after the free block 
   elif block_after_free_block["process_id"] == 0:
      block_after_free_block["start_address"] = freed_block["start_address"]
      block_after_free_block["segment_size"] += freed_block["segment_size"]
      # update block in memory map 
      memory_map[freed_block_index + 1] = block_after_free_block
      memory_map.pop(freed_block_index)
   # if just the block before the free block is free 
   elif block_before_free_block["process_id"] == 0:
      block_before_free_block["end_address"] = freed_block["end_address"]
      block_before_free_block["segment_size"] += freed_block["segment_size"]
      
      # update block in memory map
      memory_map[freed_block_index - 1] = block_before_free_block
      memory_map.pop(freed_block_index)

   # if neither before nor after is free
   else: 
    # update block before freed block
       block_before_free_block["end_address"] = freed_block["end_address"]
       block_before_free_block["segment_size"] += freed_block["segment_size"]
       # update block in memory map
       memory_map[freed_block_index + 1] = block_after_free_block
      
      # remove the free block 
       memory_map.pop(freed_block_index)

   
   for block in memory_map:
      print(block)
   # method does not have any explicit return value 
   return 