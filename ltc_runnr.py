import sys

# --- YOUR SOLUTION CLASS ---
class Solution:
    def solve(self, s:str) :
        print(s)
        return len(set(s))
        #return [int(x) * 2 for x in data]

# --- DRIVER CODE ---
def main():
    # 1. Open the input file for reading and output file for writing
    try:
        with open('input.txt', 'r') as f_in, open('output.txt', 'w') as f_out:
            
            # 2. Read lines from the input file
            # .strip() removes whitespace/newlines
            lines = [line.strip() for line in f_in.readlines() if line.strip()]
            
            # 3. Instantiate your Solution class
            sol = Solution()
            
            # 4. Process the data
            # Depending on the problem, you might pass one line or all lines
            result = sol.solve(lines)
            
            # 5. Write the result to the output file
            # If result is a list, we join it into a string
            if isinstance(result, list):
                f_out.write("\n".join(map(str, result)))
            else:
                f_out.write(str(result))
                
        print("Execution successful! Check output.txt for results.")
        
    except FileNotFoundError:
        print("Error: Please ensure 'input.txt' exists in the same directory.")

if __name__ == "__main__":
    main()