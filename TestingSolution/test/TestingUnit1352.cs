using Xunit;
using Moq;

namespace UserService.Tests
{
    public class UserManagementTests
    {
        private readonly Mock<IUserRepository> _userRepositoryMock;
        private readonly UserManagement userManagement;

        public UserManagementTests()
        {
            _userRepositoryMock = new Mock<IUserRepository>();
            userManagement = new UserManagement(_userRepositoryMock.Object);
            _userRepositoryMock.Setup(r => r.Add(It.IsAny<User>()));
            _userRepositoryMock.Setup(r => r.Delete(It.IsAny<string>()));
            _userRepositoryMock.Setup(r => r.Update(It.IsAny<User>()));
            _userRepositoryMock.Setup(r => r.GetUser(It.IsAny<string>()));
        }

        [Fact]
        public void AddUser_ValidData_ReturnsTrue()
        {
            // Arrange
            var user = new User { Name = "John", Email = "john@example.com", Password = "password" };

            // Act
            var result = userManagement.AddUser(user.Name, user.Email, user.Password);

            // Assert
            _userRepositoryMock.Verify(r => r.Add(user), Times.Once);
            Assert.True(result);
        }

        [Fact]
        public void AddUser_InvalidData_ReturnsFalse()
        {
            // Arrange
            var user = new User { Name = "", Email = "john@example.com", Password = "password" };

            // Act
            var result = userManagement.AddUser(user.Name, user.Email, user.Password);

            // Assert
            _userRepositoryMock.Verify(r => r.Add(It.IsAny<User>()), Times.Never);
            Assert.False(result);
        }

        [Fact]
        public void DeleteUser_ValidEmail_ReturnsTrue()
        {
            // Arrange
            var email = "john@example.com";

            // Act
            var result = userManagement.DeleteUser(email);

            // Assert
            _userRepositoryMock.Verify(r => r.Delete(email), Times.Once);
            Assert.True(result);
        }

        [Fact]
        public void DeleteUser_InvalidEmail_ReturnsFalse()
        {
            // Arrange
            var email = "";

            // Act
            var result = userManagement.DeleteUser(email);

            // Assert
            _userRepositoryMock.Verify(r => r.Delete(It.IsAny<string>()), Times.Never);
            Assert.False(result);
        }

        [Fact]
        public void UpdateUser_ValidData_ReturnsUser()
        {
            // Arrange
            var email = "john@example.com";
            var user = new User { Name = "John", Email = email, Password = "password" };

            // Act
            var result = userManagement.UpdateUser(email, user.Name, user.Email, user.Password);

            // Assert
            _userRepositoryMock.Verify(r => r.Update(user), Times.Once);
            Assert.NotNull(result);
        }

        [Fact]
        public void UpdateUser_InvalidData_ReturnsNull()
        {
            // Arrange
            var email = "john@example.com";
            var user = new User { Name = "", Email = email, Password = "password" };

            // Act
            var result = userManagement.UpdateUser(email, user.Name, user.Email, user.Password);

            // Assert
            _userRepositoryMock.Verify(r => r.Update(It.IsAny<User>()), Times.Never);
            Assert.Null(result);
        }

        [Fact]
        public void GetUser_ValidEmail_ReturnsUser()
        {
            // Arrange
            var email = "john@example.com";
            var user = new User { Name = "John", Email = email, Password = "password" };

            _userRepositoryMock.Setup(r => r.GetUser(email)).Returns(user);

            // Act
            var result = userManagement.GetUser(email);

            // Assert
            Assert.Equal(user, result);
        }

        [Fact]
        public void GetUser_InvalidEmail_ReturnsNull()
        {
            // Arrange
            var email = "";

            _userRepositoryMock.Setup(r => r.GetUser(email)).Returns((User)null);

            // Act
            var result = userManagement.GetUser(email);

            // Assert
            Assert.Null(result);
        }
    }

    public class User
    {
        public string Name { get; set; }
        public string Email { get; set; }
        public string Password { get; set; }
    }

    public interface IUserRepository
    {
        void Add(User user);
        void Delete(string email);
        void Update(User user);
        User GetUser(string email);
    }

    public class UserManagement
    {
        private readonly IUserRepository _userRepository;

        public UserManagement(IUserRepository userRepository)
        {
            _userRepository = userRepository;
        }

        public bool AddUser(string name, string email, string password)
        {
            if (string.IsNullOrEmpty(name) || string.IsNullOrEmpty(email) || string.IsNullOrEmpty(password))
                return false;

            var user = new User { Name = name, Email = email, Password = password };
            _userRepository.Add(user);
            return true;
        }

        public bool DeleteUser(string email)
        {
            if (string.IsNullOrEmpty(email))
                return false;

            _userRepository.Delete(email);
            return true;
        }

        public User GetUser(string email)
        {
            var user = _userRepository.GetUser(email);
            return user ?? new User();
        }

        internal object? UpdateUser(string email1, string name, string email2, string password)
        {
            throw new NotImplementedException();
        }
    }
}