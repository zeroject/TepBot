using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Domain;

namespace UserService
{
    public class UserManagment
    {
        public bool AddUser(string name, string email, string password)
        {
            // Add user to database
            if (string.IsNullOrEmpty(name) || string.IsNullOrEmpty(email) || string.IsNullOrEmpty(password))
            {
                return false;
            }
            User user = new User() 
            {
                Name = name,
                Email = email,
                Password = password
            };
            return true;
        }

        public bool DeleteUser(string email)
        {
            // Delete user from database
            if (string.IsNullOrEmpty(email))
            {
                return false;
            }
            return true;
        }

        public User UpdateUser(string email, string name, string password)
        {
            // Update user in database
            if (string.IsNullOrEmpty(email) || string.IsNullOrEmpty(name) || string.IsNullOrEmpty(password))
            {
                return null;
            }
            User user = new User()
            {
                Name = name,
                Email = email,
                Password = password
            };
            return user;
        }

        public User GetUser(string email)
        {
            // Get user from database
            if (string.IsNullOrEmpty(email))
            {
                return null;
            }
            User user = new User()
            {
                Name = "John",
                Email = email,
                Password = "password"
            };
            return user;
        }
    }
}
