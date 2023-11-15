# Quick Start
You can use `Rehearser` to build reliable unit tests quickly

----

### Development Flow:

["Rehearsal run"] --> ["Adjust interactions files"] --> ["Create Mocks"] --> ["Write Unit Tests"] --> ["Finalize Implementation"]

---

### **1. Install Rehearser**:
```bash
pip install rehearser
```
---
### **2. Creating a Rehearser Proxy**: 
- Component to be tested : `Usage`
- External services: `ProductService` , `UserService` and `Cache`

```
["Usage"] --uses--> ["ProductService"], ["UserService"] --uses--> ["Cache"]
```

- In this step, we create Rehearser Proxies for instances `ProductService()` and `UserService()`, respectively.
```python
rp_product = RehearserProxy(ProductService())
rp_user = RehearserProxy(UserService())
```
---
### **3. Generate Interactions**: 
Generate mock objects using the interactions created in the previous step:
```python
# Apply patches to UserService and ProductService
with patch(
    "rehearser_examples.examples.example1.usage.UserService",
    return_value=rp_user,
), patch(
    "rehearser_examples.examples.example1.usage.ProductService",
    return_value=rp_product,
):
    # Rehearsal run
    Usage().run_example()

    # Generate interactions files
    rp_user.set_interactions_file_directory("./raw_files/rehearser_proxy/")
    rp_user.write_interactions_to_file()

    rp_product.set_interactions_file_directory("./raw_files/rehearser_proxy/")
    rp_product.write_interactions_to_file()

```
- Notes: The interaction files are in json format, and you can adjust these thru editor manually before using these for further Mock object generation.
---
### **4. Write Unit Test**:
Unit test body:
```python
# Instantiate mock objects
mock_users = MockGenerator(
    interactions_src="./raw_files/rehearser_proxy/UserService/latest_interactions.json"
).create_mock()
mock_products = MockGenerator(
    interactions_src="./raw_files/rehearser_proxy/ProductService/latest_interactions.json"
).create_mock()

# Apply patches to UserService and ProductService
with patch(
    "rehearser_examples.examples.example1.usage.UserService",
    return_value=mock_users,
), patch(
    "rehearser_examples.examples.example1.usage.ProductService",
    return_value=mock_products,
):
    # Instantiate Usage with the mocked services
    result = Usage().run_example()

    # Insert your test assertions here
    self.assertTrue(result, "run_example() failed")
```