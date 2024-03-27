# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:44:45 2024

@author: gurpr
"""

def resource_management_example():
    resource = acquire_resource()  # Acquire some resource

    try:
        # Do something with the resource
        print("Using resource:", resource)
        result = 10 / 0  # Simulating some operation that might raise an exception
    except ZeroDivisionError:
        print("Error: Division by zero!")
    finally:
        release_resource(resource)  # Release the resource, regardless of whether an exception occurred

def acquire_resource():
    print("Acquiring resource...")
    return "Resource"  # In a real scenario, this could be acquiring a lock, opening a connection, etc.

def release_resource(resource):
    print("Releasing resource:", resource)
    # Release the resource here, e.g., releasing a lock, closing a connection, etc.

# Example usage
resource_management_example()
