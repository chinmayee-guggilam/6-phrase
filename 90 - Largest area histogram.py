'''Largest Area Histogram Problem'''
#Code
def largest_area_histogram(histogram):
    stack = []
    max_area = 0
    i = 0

    while i < len(histogram):
        if not stack or histogram[i] >= histogram[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            area = histogram[top] * (i - stack[-1] - 1 if stack else i)
            max_area = max(max_area, area)

    while stack:
        top = stack.pop()
        area = histogram[top] * (i - stack[-1] - 1 if stack else i)
        max_area = max(max_area, area)

    return max_area


# Test the function
histogram = [6, 2, 5, 4, 5, 1, 6]
result = largest_area_histogram(histogram)
print("Largest area in histogram:", result)
