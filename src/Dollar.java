public class Dollar extends Money {
    public Dollar(int amount) {
        this.amount = amount;
    }

    /**
     * Multiply the amount by the multiplier.
     * @param multiplier Multiplier of the base amount
     * @return new Dollar object with multiplied amount
     */
    public Dollar times(int multiplier) {
        return new Dollar(this.amount * multiplier);
    }
}
