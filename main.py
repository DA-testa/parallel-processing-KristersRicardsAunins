# python3
#221RDC033 Kristers Ričards Auniņš 18.grupa
def parallel_processing(n, m, data):
    threads = [(0,i) for i in range(n)]
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    for i in range(m):
        laiks = data[i]
        thread = min(threads)
        output.append((thread[1], thread[0]))
        threads.remove(thread)
        threads.append((thread[0] + laiks, thread[1]))
    return output

def main():
    # TODO: create input from keyboard
    n, m = map(int,input().split())
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    #n = 0
    #m = 0
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    #data = []
    # TODO: create the function
    data = list(map(int, input().split()))
    result = parallel_processing(n,m,data)
    # TODO: print out the results, each pair in it's own line
    for i in range(m):
        print(result[i][0], result[i][1])
    
if __name__ == "__main__":
    main()
