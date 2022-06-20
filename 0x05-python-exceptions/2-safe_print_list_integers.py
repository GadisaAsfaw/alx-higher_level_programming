def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(0, x):
        try:
            v =my_list[i]
            print("{:d}".format(v), end="")
            count += 1
        except TypeError:
            #print(f'###T{v}###')
            continue
        except ValueError:
            #print(f'###V{v}###')
            continue
        #except IndexError:
        #    break
        
        
    print()
    return (count)
