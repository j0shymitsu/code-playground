/** @param {NS} ns */
export async function main(ns) 
{
    let target = ns.getHostname();
    let minSecurity = ns.getServerMinSecurityLevel(target);
    let securityThreshold = (minSecurity < 5) ? 1.2 : 1.05;

    ns.disableLog("ALL");
    ns.clearLog();
    ns.tail();

    while(true)
    {
        let currentSecurity = ns.getServerSecurityLevel(target);
        let successfulHackChance = ns.hackAnalyzeChance(target);
        let currentMoney = ns.getServerMoneyAvailable(target);
        let maxMoney = ns.getServerMaxMoney(target);
        let percentOfMaxMoney = (currentMoney / maxMoney) * 100;

        ns.print("\n---------------------------------------")
        ns.print(`${target} Status:`);
        ns.print(`Hack Chance: ${(successfulHackChance * 100).toFixed(2)}%`);
        ns.print(`Security Level: ${currentSecurity.toFixed(2)} (Minimum: ${minSecurity})`);
        ns.print(`Money: ${ns.formatNumber(currentMoney)} / ${ns.formatNumber(maxMoney)} (${percentOfMaxMoney.toFixed(2)}%)`);
        ns.print("---------------------------------------\n\n");

        if(currentSecurity > (minSecurity * securityThreshold))
        {
            ns.print(`Weakening server [${target}]...`)
            await ns.weaken(target)
        }
        else if(currentMoney < maxMoney)
        {
            ns.print(`Growing server [${target}]...`);
            await ns.grow(target);
        }

        await ns.sleep(100);
    }      
}


