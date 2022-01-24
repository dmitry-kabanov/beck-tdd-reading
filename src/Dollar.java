public class Dollar extends Money {

    Dollar(int amount, String currency) {
        super(amount, currency);
    }

    /**
     * Multiply the amount by the multiplier.
     * @param multiplier Multiplier of the base amount
     * @return new Dollar object with multiplied amount
     */
    public Money times(int multiplier) {
        return Money.dollar(this.amount * multiplier);
    }
}
