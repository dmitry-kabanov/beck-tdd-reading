public class Franc extends Money {

    public Franc(int amount, String currency) {
        this.amount = amount;
        this.currency = currency;
    }

    /**
     * Multiply the amount by the multiplier.
     * @param multiplier Multiplier of the base amount
     * @return new Franc object with multiplied amount
     */
    public Money times(int multiplier) {
        return Money.franc(this.amount * multiplier);
    }
}
