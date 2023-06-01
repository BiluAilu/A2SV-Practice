def main():
    n,m=map(int,input().split())
    if m%n:
        print("-1")
        return
    op=0
    found=False
    if n==m:
        print(0)

    else:
        m=m/n
        print("-------------------------------")
        while m/2==m//2 and m>=n:
            op += 1
            m/=2
            print(m)
            if m==n:
                print("F")
                found=True
                break
        if not found:
            print("**************************")
            while m/3==m//3 and m>=n:
                op += 1
                m=m/3
                print(m)
                if m==n:
                    found=True
                    break



        # print(op)
        if not found:
            print(-1)
        else:
            print(op)
        
main()