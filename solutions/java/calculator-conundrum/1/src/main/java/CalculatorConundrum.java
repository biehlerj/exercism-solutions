import java.util.HashMap;
import java.util.Map;
import java.util.function.BiFunction;

class CalculatorConundrum {
    public String calculate(int operand1, int operand2, String operation) {
        int result;
        Map<String, BiFunction<Integer, Integer, Integer>> operationsMap = new HashMap<>();
        operationsMap.put("+", Integer::sum);
        operationsMap.put("-", (a, b) -> a - b);
        operationsMap.put("*", (a, b) -> a * b);
        operationsMap.put("/", (a, b) -> a / b);

        if (operation == null) {
            throw new IllegalArgumentException("Operation cannot be null");
        } else if (operation == "") {
            throw new IllegalArgumentException("Operation cannot be empty");
        } else if (!operationsMap.containsKey(operation)) {
            throw new IllegalOperationException("Operation '" + operation + "' does not exist");
        } else {
            try {
                result = operationsMap.get(operation).apply(operand1, operand2);

                return operand1 + " " + operation + " " + operand2 + " = " + result;
            } catch (ArithmeticException e) {
                throw new IllegalOperationException("Division by zero is not allowed", e);
            }
        }
    }
}