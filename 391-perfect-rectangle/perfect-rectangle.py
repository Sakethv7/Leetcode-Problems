class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        """
        Determines if the given rectangles form an exact cover of a larger rectangle.
        """
        total_area = 0
        # Start with the first rectangle's coordinates as the boundary 
        min_x, min_y = rectangles[0][0], rectangles[0][1]
        max_x, max_y = rectangles[0][2], rectangles[0][3]

        corner_count = defaultdict(int) # Dictionary to count occurrences of each corner point

        # Iterate through all rectangles
        for rect in rectangles:
            total_area += (rect[2] - rect[0]) * (rect[3] - rect[1]) #Add the area of current rectangle to the total area
            
            # Update the enclosing rectangle's boundaries
            min_x = min(min_x, rect[0])
            min_y = min(min_y, rect[1])
            max_x = max(max_x, rect[2])
            max_y = max(max_y, rect[3])

            # Count each corner of the current rectangle
            corner_count[(rect[0], rect[1])] += 1  # Bottom-left corner
            corner_count[(rect[0], rect[3])] += 1  # Top-left corner
            corner_count[(rect[2], rect[3])] += 1  # Top-right corner
            corner_count[(rect[2], rect[1])] += 1  # Bottom-right corner

        enclosing_area = (max_x - min_x) * (max_y - min_y) # Calculate the area of the enclosing rectangle

        # Check if total area matches enclosing rectangle's area
        # and if the four corners of the enclosing rectangle appear exactly once
        if (total_area != enclosing_area or
                corner_count[(min_x, min_y)] != 1 or
                corner_count[(min_x, max_y)] != 1 or
                corner_count[(max_x, max_y)] != 1 or
                corner_count[(max_x, min_y)] != 1):
            return False

        # Remove the enclosing rectangle's corners from the corner count dictionary
        del corner_count[(min_x, min_y)]
        del corner_count[(min_x, max_y)]
        del corner_count[(max_x, max_y)]
        del corner_count[(max_x, min_y)]

        # Verify that all remaining corners appear exactly 2 or 4 times
        # (indicating valid overlaps between rectangles)
        return all(count == 2 or count == 4 for count in corner_count.values())