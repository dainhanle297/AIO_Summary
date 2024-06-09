def f1_score(tp, fp, fn):
    # Check condition
    # Condition 1
    if not isinstance(tp, int):
        print("tp must be int")
        raise TypeError
    if not isinstance(fp, int):
        print("fp must be int")
        raise TypeError
    if not isinstance(fn, int):
        print("fn must be int")
        raise TypeError
    # Condition 2
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must be greater than zero")
        raise ValueError

    # Calculation
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1 = 2*precision*recall/(precision+recall)

    # Print results
    print("precision is ", precision)
    print("recall is ", recall)
    print("f1-score is ", f1)