#!/bin/bash

# Sendbird Platform SDK Python - Test Runner Script
# This script makes it easy to run various test scenarios.

set -e

# Color definitions
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function: Show help
show_help() {
    echo -e "${BLUE}Sendbird Platform SDK Python - Test Runner${NC}"
    echo ""
    echo "Usage: ./run_tests.sh [option]"
    echo ""
    echo "Options:"
    echo "  unit              - Run unit tests only (default)"
    echo "  integration       - Run integration tests only (requires environment variables)"
    echo "  all               - Run all tests"
    echo "  coverage          - Run unit tests with coverage report"
    echo "  quick             - Run quick unit tests (minimal output)"
    echo "  specific FILE     - Run specific test file"
    echo "  help              - Show this help message"
    echo ""
    echo "Examples:"
    echo "  ./run_tests.sh unit"
    echo "  ./run_tests.sh coverage"
    echo "  ./run_tests.sh specific test/test_user_api.py"
    echo "  ./run_tests.sh integration"
}

# Function: Check dependencies
check_dependencies() {
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}Error: python3 is not installed.${NC}"
        exit 1
    fi
    
    if ! python3 -m pip show pytest &> /dev/null; then
        echo -e "${YELLOW}pytest is not installed. Installing...${NC}"
        python3 -m pip install -r test-requirements.txt
    fi
}

# Function: Run unit tests
run_unit_tests() {
    echo -e "${BLUE}Running Unit Tests...${NC}"
    python3 -m pytest test/ --ignore=test/integration/ -v
    echo -e "${GREEN}✓ Unit Tests Completed${NC}"
}

# Function: Run integration tests
run_integration_tests() {
    echo -e "${BLUE}Running Integration Tests...${NC}"
    
    # Check if .env file exists
    if [ -f ".env" ]; then
        echo -e "${GREEN}Found .env file${NC}"
    fi
    
    # Run tests (conftest.py will load .env if it exists)
    python3 -m pytest test/integration/ -v
    
    # Check if tests were skipped due to missing credentials
    if [ $? -eq 5 ]; then
        echo -e "${YELLOW}Integration tests were skipped.${NC}"
        echo "Please configure credentials using one of these methods:"
        echo ""
        echo "Option 1 (Recommended): Create .env file in project root:"
        echo "  SENDBIRD_APP_ID=your_app_id"
        echo "  SENDBIRD_API_TOKEN=your_api_token"
        echo ""
        echo "Option 2: Set environment variables:"
        echo "  export SENDBIRD_APP_ID=your_app_id"
        echo "  export SENDBIRD_API_TOKEN=your_api_token"
        exit 1
    fi
    
    echo -e "${GREEN}✓ Integration Tests Completed${NC}"
}

# Function: Run tests with coverage
run_with_coverage() {
    echo -e "${BLUE}Running Unit Tests with Coverage...${NC}"
    python3 -m pytest test/ --ignore=test/integration/ \
        --cov=sendbird_platform_sdk \
        --cov-report=html \
        --cov-report=term
    echo -e "${GREEN}✓ Tests Completed${NC}"
    echo -e "${YELLOW}Coverage report: htmlcov/index.html${NC}"
}

# Function: Run quick tests
run_quick_tests() {
    echo -e "${BLUE}Running Quick Unit Tests...${NC}"
    python3 -m pytest test/ --ignore=test/integration/ -q --tb=no
    echo -e "${GREEN}✓ Quick Tests Completed${NC}"
}

# Function: Run specific test file
run_specific_test() {
    local test_file=$1
    echo -e "${BLUE}Running Specific Test: ${test_file}${NC}"
    python3 -m pytest "$test_file" -v
    echo -e "${GREEN}✓ Test Completed${NC}"
}

# Main logic
main() {
    # Check dependencies
    check_dependencies
    
    # If no arguments, run unit tests by default
    if [ $# -eq 0 ]; then
        run_unit_tests
        exit 0
    fi
    
    # Determine action based on first argument
    case "$1" in
        unit)
            run_unit_tests
            ;;
        integration)
            run_integration_tests
            ;;
        all)
            run_unit_tests
            echo ""
            run_integration_tests
            ;;
        coverage)
            run_with_coverage
            ;;
        quick)
            run_quick_tests
            ;;
        specific)
            if [ -z "$2" ]; then
                echo -e "${RED}Error: Please specify a test file.${NC}"
                echo "Example: ./run_tests.sh specific test/test_user_api.py"
                exit 1
            fi
            run_specific_test "$2"
            ;;
        help)
            show_help
            ;;
        *)
            echo -e "${RED}Error: Unknown option: $1${NC}"
            echo ""
            show_help
            exit 1
            ;;
    esac
}

# Execute script
main "$@"

