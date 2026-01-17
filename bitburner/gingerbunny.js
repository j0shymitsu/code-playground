/** @param {NS} ns */
export async function main(ns) 
{
    // let serverList = [];
    // serverList = serverList.slice(2)
    // allSevers(ns, "home")

    let target = "sigma-cosmetics";
    ns.disableLog("ALL");

    ns.clearLog();
    ns.tail();

    
    while(true)
    {
        let hackLvl = ns.getHackingLevel();
        let currentSecurity = ns.getServerSecurityLevel(target);
        let minSecurity = ns.getServerMinSecurityLevel(target);
        let successfulHackChance = ns.hackAnalyzeChance(target);
        let currentMoney = ns.getServerMoneyAvailable(target);
        let maxMoney = ns.getServerMaxMoney(target);
        let percentOfMaxMoney = (currentMoney / maxMoney) * 100;

        ns.print("\n")
        ns.print("--------------------------------");
        ns.print(target + " has a hack chance of " + (successfulHackChance * 100).toFixed(2) + "%");
        ns.print(target + " has a security level of " + currentSecurity.toFixed(2));
        ns.print(target + " currently at " + percentOfMaxMoney.toFixed(2) + "% of maximum growth");
        ns.print("\n");

        let canHack = ns.getServerRequiredHackingLevel(target) <= hackLvl;    // ternary operator

        if(!canHack)
        {   
            ns.print("Insufficient hacking level to hack [" + target + "]. A hacking level of " + ns.getServerRequiredHackingLevel(target) + " is required.");
            await ns.sleep(1000);
            continue;
        }
        
        if(currentSecurity > minSecurity * 1.1)
        {
            ns.print("Weakening server [" + target + "]...");
            await ns.weaken(target);
        }
        else if(currentMoney < (maxMoney * 0.5))
        {
            ns.print("Growing server [" + target + "]...");
            await ns.grow(target);
        }
        else if(successfulHackChance > 0.8)
        {
                ns.print("Attempting hack on server [" + target + "]...");
                await hack(ns, target);
        }

        await ns.sleep(1000);
    }      
}



async function hack(ns, target)
{
    let hackAmount = await ns.hack(target);
    if(hackAmount != 0)
    {
        ns.print("Server [" + target + "] has been hacked for $" + (hackAmount / 1e6).toFixed(2) + "m");
    }
    else
    {
        ns.print("Server [" + target + "] hack has failed!");
    }
    return 0;
}

// function allSevers(ns, server) 
// {
//     let neighbours = ns.scan(server);

//     if (serverList.includes(server)) 
//     {
//         return;
//     }

//     serverList.push(server);

//     for (let neighbour of neighbours) 
//     {
//         if (!serverList.includes(neighbour)) 
//         {
//             allSevers(neighbour);
//         }
//     }

//     serverList.sort((a, b) => ns.getServerRequiredHackingLevel(a) - ns.getServerRequiredHackingLevel(b));
// }

