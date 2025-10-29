// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// This contract is a basic implementation of the ERC-20 token standard.
contract ICEB {
    // Standard ERC-20 variables
    string public constant name = "ICEB Token";
    string public constant symbol = "ICEB";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // Mapping from address to user balances
    mapping(address => uint256) public balanceOf;

    // Mapping from owner to spender to the amount they are allowed to spend
    mapping(address => mapping(address => uint256)) public allowance;

    // Standard ERC-20 Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // The owner's address will be the one who deploys the contract (msg.sender)
    address public owner;

    // Constructor: Runs only once when the contract is deployed
    constructor(uint256 initialSupply) {
        // Set the owner to the deployer
        owner = msg.sender;
        
        // Calculate the supply, multiplying by 10^decimals
        // For example: 1,000,000,000 * (10^18)
        uint256 supplyWithDecimals = initialSupply * (10**decimals);
        
        // Assign the total supply and give it all to the contract creator
        totalSupply = supplyWithDecimals;
        balanceOf[msg.sender] = supplyWithDecimals;

        // Emit a Transfer event to signal the initial minting/transfer
        emit Transfer(address(0), msg.sender, supplyWithDecimals);
    }

    /**
     * @dev Transfers tokens from the caller's account to a recipient.
     * @param recipient The address to transfer to.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        // Require that the sender has enough tokens
        require(balanceOf[msg.sender] >= amount, "ICEB: insufficient balance");
        
        // Update balances
        balanceOf[msg.sender] -= amount;
        balanceOf[recipient] += amount;

        // Emit the Transfer event
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Sets an amount as the allowance of a spender over the caller's tokens.
     * @param spender The address to approve.
     * @param amount The amount to set as allowance.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        allowance[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one account to another using the allowance mechanism.
     * @param sender The address of the account to take the tokens from.
     * @param recipient The address to transfer the tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        // Require the sender has enough tokens
        require(balanceOf[sender] >= amount, "ICEB: insufficient balance");
        
        // Require the spender has enough allowance
        require(allowance[sender][msg.sender] >= amount, "ICEB: insufficient allowance");

        // Update balances
        balanceOf[sender] -= amount;
        balanceOf[recipient] += amount;

        // Decrease the allowance
        allowance[sender][msg.sender] -= amount;

        // Emit the Transfer event
        emit Transfer(sender, recipient, amount);
        return true;
    }
}

