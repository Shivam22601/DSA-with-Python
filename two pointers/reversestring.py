class solution:
    def reversestring(self, s):
        left = 0 
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

    
def main():
    string = input("Enter a string: ")
    s = list(string)
    obj = solution()
    obj.reversestring(s)
    print("Reversed String:", ''.join(s))

if __name__ == "__main__":
    main()