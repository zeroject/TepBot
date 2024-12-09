using System;
using Moq; // Added Moq package for mocking purposes
using Xunit; // Added XUnit namespace

namespace ConsoleApp1
{
    public class Calculator
    {
        public int Add(int a, int b)
        {
            return a + b;
        }

        public int Subtract(int a, int b)
        {
            return a - b;
        }

        public int Multiply(int a, int b)
        {
            return a * b;
        }

        public int Divide(int a, int b)
        {
            if (b == 0) throw new DivideByZeroException();
            return a / b;
        }
    }

    public class CalculatorTests
    {
        [Fact]
        public void Add_TwoPositiveNumbers_ReturnsSum()
        {
            // Arrange
            var calculator = new Calculator();

            // Act
            var result = calculator.Add(2, 3);

            // Assert
            Assert.Equal(5, result);
        }

        [Fact]
        public void Subtract_TwoNegativeNumbers_ReturnsDifference()
        {
            // Arrange
            var calculator = new Calculator();

            // Act
            var result = calculator.Subtract(-2, -3);

            // Assert
            Assert.Equal(-5, result);
        }

        [Fact]
        public void Multiply_TwoPositiveNumbers_ReturnsProduct()
        {
            // Arrange
            var calculator = new Calculator();

            // Act
            var result = calculator.Multiply(2, 3);

            // Assert
            Assert.Equal(6, result);
        }

        [Fact]
        public void Divide_TwoNonZeroNumbers_ReturnsQuotient()
        {
            // Arrange
            var calculator = new Calculator();

            // Act
            var result = calculator.Divide(4, 2);

            // Assert
            Assert.Equal(2, result);
        }

        [Fact]
        public void Divide_DivisionByZero_ThrowsException()
        {
            // Arrange
            var calculator = new Calculator();

            // Act and Assert
            Assert.Throws<DivideByZeroException>(() => calculator.Divide(4, 0));
        }

        [Fact]
        public void Add_Zero_ReturnsZero()
        {
            // Arrange
            var calculator = new Calculator();

            // Act
            var result = calculator.Add(0, 5);

            // Assert
            Assert.Equal(5, result);
        }

        [Fact]
        public void Subtract_Zero_ReturnsOriginalNumber()
        {
            // Arrange
            var calculator = new Calculator();

            // Act
            var result = calculator.Subtract(5, 0);

            // Assert
            Assert.Equal(5, result);
        }

        [Fact]
        public void Multiply_One_ReturnsOne()
        {
            // Arrange
            var calculator = new Calculator();

            // Act
            var result = calculator.Multiply(1, 2);

            // Assert
            Assert.Equal(2, result);
        }

        [Fact]
        public void Divide_ByOne_ReturnsOriginalNumber()
        {
            // Arrange
            var calculator = new Calculator();

            // Act
            var result = calculator.Divide(4, 1);

            // Assert
            Assert.Equal(4, result);
        }

        [Fact]
        public void Add_NegativeNumbers_ReturnsSum()
        {
            // Arrange
            var calculator = new Calculator();

            // Act
            var result = calculator.Add(-2, -3);

            // Assert
            Assert.Equal(-5, result);
        }

        [Fact]
        public void Subtract_NegativeNumbers_ReturnsDifference()
        {
            // Arrange
            var calculator = new Calculator();

            // Act
            var result = calculator.Subtract(-2, -3);

            // Assert
            Assert.Equal(1, result);
        }

        [Fact]
        public void Multiply_NegativeNumbers_ReturnsProduct()
        {
            // Arrange
            var calculator = new Calculator();

            // Act
            var result = calculator.Multiply(-2, -3);

            // Assert
            Assert.Equal(6, result);
        }

        [Fact]
        public void Divide_NegativeNumbers_ReturnsQuotient()
        {
            // Arrange
            var calculator = new Calculator();

            // Act
            var result = calculator.Divide(-4, 2);

            // Assert
            Assert.Equal(-2, result);
        }
    }
}