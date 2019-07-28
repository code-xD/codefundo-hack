# CodeFunDo-Hack

Welcome to the Official Idea Submission Repository for Microsoft CodeFunDo++ 2019.

## Abstract

Free and fair elections and functioning electoral systems are the quintessence of democracy. Elections are used to “ensure popular support and legitimacy for those who make governmental decisions.” An electoral system is the set of processes that determine how political candidates are elected to office. These procedures include the ballot structure, how citizens cast their votes, how those votes are tallied, and how the winners are determined. Electoral systems are important in many ways. First, they have significant political consequences. Electoral systems shape the nature of parties and party systems, and they affect the behavior of politicians and the strategies of voters. Hence, Blockchain offering more secure and reliable solutions can be utilised to ensure that elections are fair.

## Project Idea

Making an E-voter ID card generator which can be used in different online voting portals. In this project the client can file an application for creation of an E-Voter ID card unique to a user with a Blockchain based verification. This card can then be used by the client for voting in different Events. 

## Events Voting System (EVS)

### Proposed Workflow

![Screenshot from 2019-07-28 14-07-46](https://user-images.githubusercontent.com/33948877/62004613-dfac1500-b144-11e9-8e3b-02a82c909a6f.png)


1. The user files for an E-Voter ID card.

2. The Backend temporarily stores the application in the database which is then sent to the Blockchain for verification.

3. After the Blockchain successfully verifies the application it sends the data to a Human Admin for human verification and also to be stored in backend server.

4. The Admin verifies the data and sends the data to server to update the database . The human verification process runs parallel to the automated workflow making the process fast and reliable.

5. The backend server stores the E-Voter ID card which is used as a Login-Token which can be used by client to participate in different voting events.

### Cross Level Verification

- **L1 Verification**

If the Name, Age and Address submitted by the user matches with the data present in the dummy dataset then the ID card is L1 verified.

- **L2 Verification**

If the user has submitted PAN card number then the ID card is L2 verified.

- **L3 Verification**

Once the ID card is verified AT L1 and L2, it is processed for Human Admin Verification and where the card is verified at level L3 and hence, making it the most legitimate the ID card can be.

### Reliable and Secure Authentication
The authorization is token based which means while logging in the credentials are verified with a third party application which uses OTP generation as its medium for logging in thus a two-way authentication system is incorporated which is further more secure.


## Further Notes and Assumptions 

The dataset used is a developer created dataset to verify the details submitted by the client. This has been done to simulate a government based database which be can used to verify the information submitted and thus making the application very realistic. We are going to use Azure Blockchain Workbench and REST based APIs manually developed to communicate at different levels. The backend is going to be based on Django Web Framework and the frontend will be a user focused website to be used by the client.
