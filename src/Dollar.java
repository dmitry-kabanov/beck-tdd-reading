public class Dollar extends Money {

    public Dollar(int amount) {
        this.amount = amount;
        this.currency = "USD";
    }

    /**
     * Multiply the amount by the multiplier.
     * @param multiplier Multiplier of the base amount
     * @return new Dollar object with multiplied amount
     */
    public Money times(int multiplier) {
        return new Dollar(this.amount * multiplier);
    }
}
