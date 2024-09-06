import streamlit as st

# Define the fare function
def fare(d):
    book = 2.0   # Booking fee
    start = 3.0  # Starting fee
    cost = 1.0   # Cost per distance unit
    total_fare = book + start + d * cost
    return total_fare

# Streamlit application
def main():
    st.title("Fare Calculator")
    
    # Input for distance
    d = st.number_input("What is the distance (in units)?", min_value=0.0, step=0.1)
    
    # Calculate fare when the button is clicked
    if st.button("Calculate Fare"):
        if d >= 0:
            total_fare = fare(d)
            st.success(f"The total fare for a distance of {d} units is: ${total_fare:.2f}")
        else:
            st.error("Please enter a valid distance.")

# Run the application
if __name__ == "__main__":
    main()
    
