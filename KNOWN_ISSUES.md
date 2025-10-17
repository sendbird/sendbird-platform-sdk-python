# Known Issues - Sendbird Platform SDK Python

This document tracks known issues and bugs in the SDK that are reflected in failing tests.

## Optional Fields Rejecting None Values

**Status**: 🐛 Bug  
**Severity**: Medium  
**Affected Version**: 2.1.1

### Description

Optional fields in model classes incorrectly reject `None` values. According to OpenAPI specification and general API best practices, optional fields should accept `None` values, but the current SDK implementation raises `ApiTypeError` when `None` is explicitly passed to optional fields.

### Expected Behavior

```python
# This SHOULD work for optional fields
model = CreateAUserRequest(
    nickname="John Doe",
    profile_url="https://example.com/profile.jpg",
    user_id="user123",
    discovery_keys=None,  # Optional field - should accept None
    metadata=None         # Optional field - should accept None
)
```

### Actual Behavior

```python
# This currently FAILS with ApiTypeError
model = CreateAUserRequest(
    nickname="John Doe",
    profile_url="https://example.com/profile.jpg",
    user_id="user123",
    discovery_keys=None  # ❌ Raises: Invalid type for variable 'discovery_keys'
)
```

### Workaround

Instead of passing `None`, simply omit the field:

```python
# ✅ This works
model = CreateAUserRequest(
    nickname="John Doe",
    profile_url="https://example.com/profile.jpg",
    user_id="user123"
    # discovery_keys and metadata omitted - works fine
)
```

Or use empty values:

```python
# ✅ This also works
model = CreateAUserRequest(
    nickname="John Doe",
    profile_url="https://example.com/profile.jpg",
    user_id="user123",
    discovery_keys=[],  # Empty list instead of None
    metadata={}         # Empty dict instead of None
)
```

### Affected Models

The following models have optional fields that incorrectly reject `None`:

1. **AcceptAnInvitationRequest**
   - `access_code` (optional but not nullable)

2. **CreateAUserRequest**
   - `discovery_keys` (optional but not nullable)
   - `metadata` (optional but not nullable)
   - `profile_file` (optional but not nullable)

3. **SendbirdUser**
   - `nickname` (optional but not nullable)
   - `profile_url` (optional but not nullable)
   - `discovery_keys` (optional but not nullable)
   - `preferred_languages` (optional but not nullable)
   - `session_tokens` (optional but not nullable)
   - `metadata` (optional but not nullable)
   - **Exception**: `state` field IS nullable (correctly accepts None)

### Failing Tests

The following tests document this issue and currently fail:

```bash
# Run these tests to see the issue
pytest test/test_accept_an_invitation_request.py::TestAcceptAnInvitationRequest::testAcceptAnInvitationRequestOptionalFieldShouldAcceptNone -v
pytest test/test_create_a_user_request.py::TestCreateAUserRequest::testCreateAUserRequestOptionalDiscoveryKeys -v
pytest test/test_create_a_user_request.py::TestCreateAUserRequest::testCreateAUserRequestOptionalMetadata -v
pytest test/test_sendbird_user.py::TestSendbirdUser::testSendbirdUserOptionalFields -v
```

Test results:
```
FAILED test/test_accept_an_invitation_request.py - ApiTypeError: Invalid type for variable 'access_code'
FAILED test/test_create_a_user_request.py (multiple) - ApiTypeError for optional fields
FAILED test/test_sendbird_user.py (multiple) - ApiTypeError for optional fields

7 failed, 244 passed
```

### Root Cause

This issue likely stems from the OpenAPI Generator configuration or template. The generator is not properly marking optional fields as nullable in the generated Python code.

In the model files, optional non-nullable fields are defined as:
```python
'discovery_keys': ([str],),  # Should be ([str], none_type,) for nullable
```

While properly nullable fields are defined as:
```python
'state': (str, none_type,),  # ✅ Correctly includes none_type
```

### Potential Solutions

1. **Update OpenAPI Generator Templates**
   - Modify the Python generator template to mark optional fields as nullable
   - Location: `sendbird-platform-openapi/` generator configuration

2. **Update OpenAPI Specification**
   - Explicitly mark optional fields as `nullable: true` in the YAML spec
   - Location: `sendbird-platform-openapi/sendbird.yaml`

3. **Post-Processing Script**
   - Create a script to automatically add `none_type` to optional fields after generation
   - Similar to existing `post_process_nullable_fields_auto.py`

### Recommendation

Update the OpenAPI specification or generator configuration to properly handle optional fields:

```yaml
# In sendbird.yaml
properties:
  discovery_keys:
    type: array
    items:
      type: string
    nullable: true  # Add this for optional fields
```

### References

- OpenAPI Specification: [Nullable](https://swagger.io/docs/specification/data-models/data-types/#null)
- Python OpenAPI Generator: [Issues with nullable](https://github.com/OpenAPITools/openapi-generator/issues?q=nullable+python)
- Related test files:
  - `test/test_accept_an_invitation_request.py`
  - `test/test_create_a_user_request.py`
  - `test/test_sendbird_user.py`

---

**Last Updated**: 2025-10-16  
**Reported By**: Automated Test Suite  
**Priority**: Medium - Affects developer experience but has workarounds

