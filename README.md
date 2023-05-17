# Project 3: Estate Planning DApp

Code developed by Andrew Bader, Trent Ransom, Halam Kim, and Max Accurso

## Table of Contents
1. [Installation Instructions](#Installation)
2. [Introduction](#Introduction)
3. [Background Information](#Background)
4. [Platform Description](#Platform)
5. [Future Vision, and Cost Estimation](#Future)
6. [Project Operations](#Operations)
    - a. [Technologies Used](#Technologies)
    - b. [Problems and Solutions](#Problems)
    - c. [Results](#Results)
7. [Conclusion](#Conclusion)

## 1. Installation Instructions <a name="Installation"></a>

To clone and use:
1) make a local directory for this github repository
2) clone down this repo with git clone command
3) cd into cloned repo
4) activate conda development environment
5) install necessary dependencies via the following commands:
    ```
    pip install web3 
    pip install streamlit
    pip install python-dotenv 
    pip install requests 
    ```
6) create .env file in the final_app repo and input the following information:

WEB3_PROVIDER_URI: The URI of the Ethereum node provider
SMART_CONTRACT_ADDRESS: The address of the deployed smart contract
PINATA_API_KEY: Pinata API key
PINATA_SECRET_API_KEY: Pinata secret API key

7) cd into the final_app repo

8) start up ganache local instance
9) start up streamlit app
   ``` 
   streamlit run app.py
   ```
10) look for app in browser client at Local URL 
11) follow app instructions

## 2. Introduction <a name="Introduction"></a>

Blockchain technology holds immense potential for lawyers and should not be overlooked. As mainstream adoption of blockchain is on the horizon, it brings forth abundant opportunities for lawyers to expand their practice. By embracing blockchain, lawyers can streamline and simplify their transactional work, digitally sign legal agreements, and securely store them in an immutable manner. Leveraging scripted text, smart contracts, and automated contract management allows for a significant reduction in time spent on preparing and customizing standard legal documents. These time and cost savings can ultimately be passed on to clients, making legal services more affordable.

Furthermore, blockchain technology promotes accessibility and inclusivity in the justice system by reducing complexity for consumers and lowering exorbitant legal fees. The utilization of distributed ledger technology enables the creation of a shared ledger that is accessible to all parties involved in an agreement. Blockchain-based contracts inherently ensure compliance, leaving no room for surprises or misinterpretation. This aspect also enables non-technologists to better comprehend the transactions they engage in and understand the underlying principles of smart contracts.

By embracing blockchain, lawyers can enhance their efficiency, provide cost-effective services, and foster greater transparency and understanding among their clients. It is crucial for legal professionals to recognize and embrace the potential of blockchain technology in order to stay ahead in an evolving legal landscape.

## 3. Background Information <a name="Platform"></a>

#### <u>Estate Planning</u>

Estate planning encompasses the crucial task of determining the preservation, management, and distribution of an individual's assets following their passing. It also considers the management of properties and financial obligations in the event of incapacitation. Contrary to popular belief, estate planning is not solely reserved for the ultra-wealthy; it is a process that anyone can and should consider.
An individual's estate may consist of various assets, such as properties, vehicles, stocks, artwork, life insurance, pensions, and debts. There are numerous reasons why individuals engage in estate planning, including preserving family wealth, providing for a surviving spouse and children, funding education for children or grandchildren, or leaving a charitable legacy.

During the estate planning process, certain documents are essential. Common examples include wills, powers of attorney (POAs), guardianship designations, and living wills. Additionally, gathering and organizing documents such as bank and account statements, comprehensive lists of holdings (assets and liabilities), and beneficiary designations is helpful. A will is a legal document that outlines how an individual's property and custody of minor children, if applicable, should be handled after their passing. It allows the individual to express their wishes and appoint a trusted trustee or executor to carry out those intentions. The validity of a will is determined through a legal process called probate, which involves the administration of the deceased person's estate and the distribution of assets to beneficiaries. Within 30 days of the testator's death, the custodian of the will must submit it to the probate court or the named executor.

Estate planning is an ongoing process that should commence as soon as an individual possesses any significant assets. As life progresses and goals evolve, the estate plan should adapt accordingly. Insufficient estate planning can place undue financial burdens on loved ones, as estate taxes can be as high as 40%. Therefore, at the very least, it is crucial to establish a will, even if the taxable estate is not substantial. The cost of estate planning varies depending on the steps taken and the chosen approach. Hiring an estate planner or lawyer may involve hourly fees, although some professionals may offer a flat fee for their services. Additional costs can include will preparation, which can range from as low as $100 when seeking assistance from a professional.

#### Associated Challenges

Our platform was developed with the aim of tackling the challenges associated with estate planning. The following checklist serves as a valuable tool to ensure that crucial aspects are not overlooked. Each of these issues requires careful consideration, as they can lead to significant problems if left unaddressed.

**Family Harmony:** Estate planning is an opportunity to demonstrate your care for loved ones. However, choices regarding executors or trustees can bring up past conflicts and negative emotions for those not selected. Considering ways to mitigate and resolve these conflicts, or at least minimize exacerbating them, can help avoid family disputes.

**Procrastination:** Procrastination is a common stumbling block in estate planning. Delaying the process can result in significant challenges and increased expenses if disability or death occurs without proper planning.

**Attorney's Fees:** Controlling legal fees is best achieved by engaging in planning while you are alive and capable of overseeing the process. Failing to plan is likely to increase the overall fees paid, particularly if family members resort to litigation to settle disputes after your passing.

**Successor Fiduciaries:** Ensure you name backup executors and trustees or establish a mechanism for beneficiaries to fill vacant roles, eliminating the need for court intervention.

**Probate:** Going through court-supervised estate administration is typically an arduous process. Despite the assistance of court personnel, there are filing fees, concerns about privacy, and lengthy waiting periods before asset distribution, assuming everything goes smoothly.

**Updating Beneficiary Designations:** Beneficiary designations for life insurance policies and retirement accounts are crucial. These designations are typically made when purchasing the policy or opening the account, and they need to be regularly reviewed and updated. It's not uncommon to find outdated designations that still list former spouses many years after divorce and remarriage.

**Asset Protection:** Many individuals fail to take advantage of asset protection opportunities offered through basic estate planning. Creating trusts for spouses and children, with appropriate provisions, can safeguard assets from creditors and potential threats for an extended period. While we hope our children won't experience divorce, addressing this aspect of asset protection is essential.

**Tax Planning:** Navigating the complexities of various tax systems is never easy. There is often a delicate balance between gift planning (transferring assets to minimize estate value) and preserving basis for capital gains purposes. Mishandling this issue can result in significant financial implications.

**Joint Accounts:** Joint accounts are often used for convenience during life and sometimes mistaken as a substitute for a will upon death. It's important to ensure that these accounts align with your overall plan for passing assets to your heirs. Relying on one child to distribute funds among siblings from a joint account after your passing can lead to complications.

**Contingent Beneficiaries:** Plan for contingencies in the event that immediate family members are unable to inherit your estate due to their passing. Designate alternative beneficiaries, such as charities or more distant relatives or close friends.

By addressing these issues and taking proactive steps, you can navigate estate planning more effectively, minimize potential problems, and protect your assets and loved ones.

## 4. Platform Description <a name="Platform"></a>

#### Blockchain Applications in the Legal Industry

Blockchain technology offers the potential to revolutionize various processes within the legal industry, enhancing efficiency, productivity, and security while preserving judicial authority. By optimizing different aspects of the legal and financial sectors, blockchain can reduce friction, lower costs, and automate manual tasks involved in drafting and amending legal documents. The introduction of smart contracts accelerates transactions between parties while minimizing costs. Automated and transparent management of escrow accounts using cost-efficient algorithms decreases expenses associated with manual labor, ultimately increasing the accessibility and demand for legal services.

Administrative tasks, which consume a significant portion of lawyers' time, can be automated through the use of a legal agreement repository and pre-fabricated smart contracts. Streamlining non-billable administrative tasks and transactional work not only saves time but also reduces costs for clients. Storing legal information on a decentralized, distributed ledger ensures data integrity and security, mitigating risks associated with hacking and tampering.

Through our platform, we aim to address the aforementioned challenges by leveraging blockchain technology in various applications such as electronic signatures, timestamps, non-fungible tokens (NFTs), distributed ledgers, and tokenization. Electronic signatures offer speed, efficiency, and cost savings compared to traditional authentication processes. Signing on the blockchain significantly reduces costs compared to e-signature platforms and facilitates independent verification without compromising content confidentiality.

NFTs enable the representation of unique digital assets on the blockchain, providing robust property rights in the digital realm. Blockchain-based IP enforcement systems empower creators to protect their work and monitor its usage. By registering and selling properties on the blockchain, property owners can bypass costly intermediaries, leading to transparent and immutable property rights management and a reduction in transaction costs.

Blockchain technology can also enhance the chain of custody process, ensuring the integrity of evidence by generating and tracking unique evidence tokens stored in a public/private blockchain. This reduces opportunities for tampering and provides a verifiable record of evidence movements.

Tokenization allows for the conversion of asset rights into digital tokens, facilitating fractional ownership and enabling creators to legally sell fractions of their assets on platforms supporting smart contracts.

Through these blockchain applications, we aim to revolutionize the legal industry and overcome its challenges, delivering increased efficiency, security, and cost savings for all stakeholders involved.

#### Platform Breakdown

In order to facilitate a seamless transition of your assets and financial affairs in the event of your passing, it is crucial to undertake a series of steps and considerations, all of which our platform can assist you with. Firstly, compile a comprehensive inventory of all your assets, encompassing physical possessions such as real estate and precious metals, as well as bank accounts, insurance policies, and annuities. Similarly, create a record of your outstanding debts, including loans and financial obligations. Once you have these inventories, you will no longer need to make physical copies if multiple beneficiaries require access to the information; our technology will handle that task for you.

Next, carefully review your retirement accounts, paying special attention to those that have designated beneficiaries. Keep in mind that accounts with designated beneficiaries pass directly to them, regardless of the directives stated in your will. It is equally important to review your insurance policies and annuities, ensuring that your beneficiary information is up to date and all other details are accurate. You may also want to consider establishing joint accounts or utilizing transfer-on-death designations, as these measures can help bypass the probate process. Joint accounts, such as checking and savings accounts, with a right of survivorship allow for the seamless transfer of ownership to the surviving account holder. Additionally, transfer-on-death designations enable you to designate an individual who can assume control of the account upon your passing, without the need for probate. One remarkable aspect of our platform is that you will have constant access to these details, allowing you to update them at your convenience.

Selecting an estate administrator is a critical decision. Choose someone you trust to handle your financial affairs after your passing. While your spouse may appear to be a natural choice, consider their emotional state and whether they are the most suitable person for this responsibility. If you feel uncertain about making this decision, we can act as the administrator on your behalf, ensuring that all matters are properly attended to.

Another essential step is the creation of your will. Wills not only clarify any financial uncertainties but also provide instructions regarding the care of minor children, pets, and the allocation of funds for charitable donations. Regularly review your will and associated documents every few years to ensure they accurately reflect your current wishes, making any necessary adjustments. It's important to note that your will would be automatically generated as you progress through the preceding steps.

By following these steps and considerations through our platform, you can establish a well-structured plan for managing your assets and financial affairs, providing both yourself and your loved ones with peace of mind.

## 5. Future Vision and Cost Estimation <a name="Future"></a>

In our future vision, we aim to continually improve and expand our blockchain-based estate planning platform based on user feedback and evolving technologies. We recognize that the legal landscape is constantly evolving, and we are committed to staying at the forefront of these changes.

One key aspect of our future vision is to expand the platform's offerings beyond estate planning. While estate planning is our initial focus, we understand that individuals and legal professionals have broader legal needs. We plan to incorporate additional legal services into our platform, such as contract management, intellectual property protection, and dispute resolution. By expanding our service offerings, we aim to provide a comprehensive solution that caters to various legal needs.

We also recognize the growing importance of mobile devices in our daily lives. To enhance accessibility and convenience for our users, we intend to develop mobile applications for our platform. This will enable users to engage with our services on-the-go, allowing them to manage their estate planning and legal affairs conveniently from their smartphones or tablets.

Furthermore, strategic partnerships with legal professionals will be a key component of our future vision. We aim to collaborate with lawyers, estate planners, and other legal experts to offer value-added services to our users. These partnerships will allow us to provide expert advice, personalized consultations, and tailored solutions to meet the specific needs of our users. By working closely with legal professionals, we can ensure that our platform remains aligned with the latest legal requirements and best practices.
As we expand our platform and services, we also envision exploring international markets. Estate planning and legal needs vary across different jurisdictions, and we plan to adapt our platform to accommodate the legal frameworks of various countries. This expansion will not only broaden our user base but also provide individuals and legal professionals around the world with access to efficient and secure estate planning solutions.

Throughout our journey, we will continue to prioritize innovation and adaptability. We will closely monitor emerging technologies, such as artificial intelligence and machine learning, and explore how they can further enhance our platform and user experience. By embracing innovation and leveraging cutting-edge technologies, we can continue to revolutionize the legal industry and provide our users with the most advanced and efficient estate planning solutions available.

To summarize, our future vision for the blockchain-based estate planning platform involves expanding our service offerings, developing mobile applications, establishing strategic partnerships, exploring international markets, and embracing innovation. By pursuing these initiatives, we aim to create a future where estate planning and legal services are accessible, efficient, and secure, empowering individuals and legal professionals to navigate the complexities of the legal landscape with confidence.

## 6. Project Operations <a name="Operations"></a>

### a. Technologies Used <a name="Technologies"></a>

For this project we utilized a number of technologies. We used the Python programming language for the majority of the functionality of the application and its components. We used python to implement front end design paradigms such as input fields for addresses and asset parameters. We chose to use the Streamlit open-source framework for building our blockchain app in Python. Streamlit was utilized for the development of our user friendly UI for the will asset application. We also used the Web3.py Python library to enable our app's interaction with the Ethereum blockchain. This library was used to connect this app to the blockchain network. This library enables loading of the contract ABI (Application Binary Interface), interaction with the backend Solidity smart contract, in addition to the execution of transactions. Pinata was used also in the application to provide easy access to IPFS (InterPlanetary File System) functionality such uploading files to the IPFS and obtaining the resultant IPFS hash. We also used the Solidity programming language for writing smart contracts specifically for the Ethereum blockchain. We compiled these contracts with the open source Remix IDE and generated resultant smart contract ABI json files. These json files are utilized to run the streamlit app.py instances. Solidity and remix was is to deploy and run the backend of this will-asset application. Ganache was used to emulate a local blockchain environment for testing of this app.

### b. Problems and Solutions <a name="Problems"></a>

### c. Results <a name="Results"></a>

## 6. Conclusion <a name="Conclusion"></a>

The potential of blockchain technology in the legal industry is immense and should not be ignored. Embracing blockchain can revolutionize the way lawyers streamline transactional work, simplify legal agreements, and enhance security. By leveraging smart contracts, scripted text, and automated management, lawyers can save time and costs, which can ultimately benefit their clients by making legal services more affordable and accessible.

Estate planning, a crucial aspect of financial management, should be undertaken by individuals regardless of their wealth. Proper estate planning ensures the preservation, management, and distribution of assets, while also addressing key issues such as probate, asset protection, tax planning, family harmony, attorney's fees, successor fiduciaries, contingent beneficiaries, and beneficiary designations.

Our platform aims to address these challenges by providing a comprehensive checklist and utilizing blockchain applications such as electronic signatures, NFTs, distributed ledgers, and tokenization. These technologies offer efficiency, transparency, and security in estate planning and asset management.

Through our platform, users can create an organized plan for their financial affairs, ensuring a smooth transition for their assets and providing peace of mind for themselves and their loved ones. By recognizing the potential of blockchain technology and embracing its applications in the legal industry, lawyers can enhance their practice and deliver more efficient and cost-effective services.

The future of estate planning and legal services lies in embracing innovative technologies, and our platform is designed to support individuals and legal professionals on this journey. By adopting blockchain, we can pave the way for a more secure, accessible, and transparent legal landscape.
