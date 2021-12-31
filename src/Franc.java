public class Franc {
    /**
        Class for handling dollar currency.
     */
    private int amount;

    public Franc(int amount) {
        this.amount = amount;
    }

    /**
     * Multiply the amount by the multiplier.
     * @param multiplier Multiplier of the base amount
     * @return new Franc object with multiplied amount
     */
    public Franc times(int multiplier) {
        return new Franc(this.amount * multiplier);
    }

    public boolean equals(Object obj) {
        Franc dollar = (Franc) obj;
        return amount == dollar.amount;
    }
}
