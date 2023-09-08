public class Local {
    private boolean available;

    // Constructor to initialize the availability property
    public Local(boolean available) {
        this.available = available;
    }

    // Getter method to check availability
    public boolean isAvailable() {
        return available;
    }

    // Setter method to update availability
    public void setAvailable(boolean available) {
        this.available = available;
    }

    public static void main(String[] args) {
        // Create an instance of the Local class
        Local local1 = new Local(true);

        // Check if the local is available
        if (local1.isAvailable()) {
            System.out.println("The local is available.");
        } else {
            System.out.println("The local is not available.");
        }

        // Set the local's availability to false
        local1.setAvailable(false);

        // Check again
        if (local1.isAvailable()) {
            System.out.println("The local is available.");
        } else {
            System.out.println("The local is not available.");
        }
    }
}
