using System;
using Moq;
using Xunit;

using ConsoleApp1; // Add this line

namespace test
{
    public class CalculatorTests
    {
        [Fact]
        public void Add_ReturnsCorrectResult()
        {
            // Arrange
            var calculator = new Calculator();
            int a = 5;
            int b = 3;

            // Act
            int result = calculator.Add(a, b);

            // Assert
            Assert.Equal(8, result);
        }

        [Fact]
        public void Subtract_ReturnsCorrectResult()
        {
            // Arrange
            var calculator = new Calculator();
            int a = 5;
            int b = 3;

            // Act
            int result = calculator.Subtract(a, b);

            // Assert
            Assert.Equal(2, result);
        }

        [Fact]
        public void Multiply_ReturnsCorrectResult()
        {
            // Arrange
            var calculator = new Calculator();
            int a = 5;
            int b = 3;

            // Act
            int result = calculator.Multiply(a, b);

            // Assert
            Assert.Equal(15, result);
        }

        [Fact]
        public void Divide_ReturnsCorrectResult()
        {
            // Arrange
            var calculator = new Calculator();
            int a = 5;
            int b = 3;

            // Act
            int result = calculator.Divide(a, b);

            // Assert
            Assert.Equal(1, result);
        }

        [Fact]
        public void Divide_ByZero_ThrowsException()
        {
            // Arrange
            var calculatorMock = new Mock<Calculator>();
            calculatorMock.Setup(c => c.Add(It.IsAny<int>(), It.IsAny<int>())).Returns(0);
            calculatorMock.Setup(c => c.Subtract(It.IsAny<int>(), It.IsAny<int>())).Returns(0);
            calculatorMock.Setup(c => c.Multiply(It.IsAny<int>(), It.IsAny<int>())).Returns(0);

            // Act and Assert
            Assert.Throws<DivideByZeroException>(() => calculatorMock.Object.Divide(5, 0));
        }
    }
}