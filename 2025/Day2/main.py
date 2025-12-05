def main():
    answer = 0 
    ranges_to_check = set() 

    with open('input', 'r') as input_file:
        for line in input_file.readlines():
            for id_range in line.strip().split(','):
                if id_range != '':
                    ids_start_stop = id_range.split('-')
                    start, stop = int(ids_start_stop[0]), int(ids_start_stop[1])
                    ranges_to_check.add((start, stop))

    for id_range in ranges_to_check:
        id_range_start = id_range[0]
        id_range_stop = id_range[1] 

        for product_id in range(id_range_start, id_range_stop+1):
            product_id_str = str(product_id)
            test_case_sequences = create_sequences_to_test(product_id_str)

            for test_case in test_case_sequences:
                # use split to remove any matching sequences from the product_id
                test_output = product_id_str.split(test_case)
                output_validity = True
                for item in test_output:
                    if item != '':
                        # a good sequence won't have any values besides ''
                        output_validity = False
                        break
                if output_validity is True:
                    answer = answer + product_id 
                    # break otherwise it will add product_id like '2222' twice
                    # because '2' and '22' are valid sequences for that product_id
                    break
    return answer


def create_sequences_to_test(curr_id: str):
    midIdx = len(curr_id)//2
    testSequences = []
    for i in range(1, midIdx+1):
        newSequenceToTest = curr_id[:i]
        testSequences.append(newSequenceToTest)
    return testSequences


if __name__ == '__main__':
    print(main())