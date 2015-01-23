def get_meaing(term):
    index = 1
    wanted_index = -1
    while index < len(tech_list)-1:
        if tech_list[index].term == term:
            wanted_index = index
        index = index + 1
    if wanted_index != -1:
        return tech_list[index].meaning
    else:
        return 'not listed'
