// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Script, console} from "forge-std/Script.sol";
import {NFT} from "../src/NFT.sol";


contract NFTScript is Script {
    NFT public nft;

    function setUp() public {}

    function run() public {
        vm.startBroadcast();

        counter = new NFT();

        vm.stopBroadcast();
    }
}
