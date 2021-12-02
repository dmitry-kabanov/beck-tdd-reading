public class Dollar {
    /**
        Class for handling dollar currency.
     */
    public int amount;

    public Dollar(int amount) {
        this.amount = amount;
    }

    /**
     * Multiply the amount by the multiplier.
     * @param multiplier Multiplier of the base amount
     */
    public void times(int multiplier) {
        this.amount *= multiplier;
    }
}
