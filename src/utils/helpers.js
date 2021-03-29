export const roundUp = (number) => {
    if (Number.isInteger(number)) {
        return number;
    }
    return number.toFixed(3);
}