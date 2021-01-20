def is_wellformed(expr) : 
    stack = [] 
  
    for char in expr: 
        if char in ["(", "{", "["]: 
  
            stack.append(char) 
        else: 
  
    
            if not stack: 
                return False
            current_char = stack.pop() 
            if current_char == '(': 
                if char != ")": 
                    return False
            if current_char == '{': 
                if char != "}": 
                    return False
            if current_char == '[': 
                if char != "]": 
                    return False
  
    # Check Empty Stack 
    if stack: 
        return False
    return True

print(is_wellformed("((())"))