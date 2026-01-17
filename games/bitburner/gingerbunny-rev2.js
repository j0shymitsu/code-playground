/** @param {NS} ns */
export async function main(ns) 
{
    // let serverList = [];
    // serverList = serverList.slice(2)
    // allSevers(ns, "home")
    let target = "iron-gym";

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

        ns.print("\n---------------------------------------")
        ns.print(`${target} Status:`);
        ns.print(`Hack Chance: ${(successfulHackChance * 100).toFixed(2)}%`);
        ns.print(`Security Level: ${currentSecurity.toFixed(2)} (Minimum: ${minSecurity})`);
        ns.print(`Money: ${ns.formatNumber(currentMoney)} / ${ns.formatNumber(maxMoney)} (${percentOfMaxMoney.toFixed(2)}%)`);
        ns.print("---------------------------------------\n");

        let requiredHackLevel = ns.getServerRequiredHackingLevel(target);

        if(requiredHackLevel > hackLvl)
        {   
            ns.print(`Insufficient hacking level for [${target}]. Required: ${requiredHackLevel}`);
            await ns.sleep(5000);
            continue;
        }

        if(currentSecurity > (minSecurity * 1.1))
        {
            ns.print(`Weakening server [${target}]...`)
            await ns.weaken(target)
        }
        else if((successfulHackChance === 1.0) && (currentMoney === maxMoney))
        {
            ns.print(`Attempting hack on server [${target}]...`);
            await hack(ns, target);
        }
        else if(currentMoney < maxMoney)
        {
            ns.print(`Growing server [${target}]...`);
            await ns.grow(target);
        }
        else if(successfulHackChance >= 0.9)
        {
            ns.print(`Attempting hack on server [${target}]...`);
            await hack(ns, target);
        }
        else
        {
            ns.print("Server conditions not optimal for hack. Adjusting...");
            await ns.sleep(5000);
        }

        await ns.sleep(100);

        // if(currentSecurity > minSecurity * 1.1)
        // {
        //     ns.print("Weakening server [" + target + "]...");
        //     await ns.weaken(target);
        // }
        // else if(currentMoney < (maxMoney * 0.5))
        // {
        //     ns.print("Growing server [" + target + "]...");
        //     await ns.grow(target);
        // }
        // else if(successfulHackChance > 0.8)
        // {
        //         ns.print("Attempting hack on server [" + target + "]...");
        //         await hack(ns, target);
        // }

        // await ns.sleep(1000);
    }      
}

async function hack(ns, target)
{
    let hackAmount = await ns.hack(target);
    if(hackAmount !== 0)
    {
        ns.print(`HACK SUCCESSFUL ON [${target}] FOR ${ns.formatNumber(hackAmount)}`);
    }
    else
    {
        ns.print(`HACK FAILURE ON [${target}]`);
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

