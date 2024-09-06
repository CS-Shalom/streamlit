import streamlit as st

# Define the fare calculation function
def calculate_fare(name, distance, age):
    # Initialize base costs
    booking_fee = 3.0
    starting_fee = 2.0
    cost = 0.0

    # Calculate cost based on distance
    if distance < 5:
        cost = 2.0 * distance
    elif 5 <= distance < 10:
        cost = 2.0 * 5 + 1.5 * (distance - 5)
    else:  # distance >= 10
        cost = 2.0 * 5 + 1.5 * 5 + 1.0 * (distance - 10)

    # Calculate total fare
    total_fare = booking_fee + starting_fee + cost

    # Apply discount for seniors (age > 60)
    if age > 60:
        total_fare *= 0.9  # Apply a 10% discount

    # Round the fare to one decimal place
    total_fare = round(total_fare, 1)

    return total_fare

# Streamlit application
def main():
    st.title("Taxi Fare Calculator")

    # Input for user details
    name = st.text_input("What is your name:")
    distance = st.number_input("How long is the distance traveled (in km):", min_value=0.0, step=0.1)
    age = st.number_input("How old are you?", min_value=0, step=1)

    # Calculate fare when the button is clicked
    if st.button("Calculate Fare"):
        if name and distance >= 0 and age >= 0:
            total_fare = calculate_fare(name, distance, age)
            st.success(f"{name}, your taxi fare is ${total_fare:.1f}")
        else:
            st.error("Please provide valid inputs.")

# Run the application
if __name__ == "__main__":
    main()
    