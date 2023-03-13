# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    for i in range(m):
        laiks = data[i]
        thread = heapq.heappop(threads)
        output.append((thread[1], thread[0]))
        heapq.heappush(threads, (thread[0] + laiks, thread[1]))

    return output

def main():
    # TODO: create input from keyboard
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
    n, m = map(int,input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n,m,data)
    for i in range(m):
        print(result[i][0], result[i][1])
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
