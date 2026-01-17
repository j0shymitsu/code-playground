/** @param {NS} ns */
export async function main(ns) 
{
    ns.disableLog("ALL");
    ns.clearLog();
    ns.tail();

    let serverList = [];

    // recursive function to get all servers
    function allServers(server) 
    {
        let neighbours = ns.scan(server);

        if (serverList.includes(server)) 
        {
            return;
        }

        if(!server.includes("server"))
        {
            serverList.push(server);
        }

        for (let neighbour of neighbours) 
        {
            if (!serverList.includes(neighbour)) 
            {
                allServers(neighbour);
            }
        }


        serverList.sort((a, b) => ns.getServerRequiredHackingLevel(a) - ns.getServerRequiredHackingLevel(b));
    }

    // loop to always check against current hack level and apply port openers
    while(true)
    {
        serverList = [];
        allServers("home");
        ns.print("Discovered servers: " + serverList.join(", "))

        let hackLvl = ns.getHackingLevel();

        for(let i = 0; i < serverList.length; i++)
        {
            let currentTarget = serverList[i]
            // ns.print(`server_name = ${serverList[i]}\nhack_level = ${ns.getServerRequiredHackingLevel(serverList[i])}\n\n`);
            if(ns.getServerNumPortsRequired(currentTarget) > 0 && !ns.hasRootAccess(currentTarget))
            {
                await ns.brutessh(currentTarget);
                await ns.ftpcrack(currentTarget);
                await ns.relaysmtp(currentTarget);
                await ns.httpworm(currentTarget);
                await ns.sqlinject(currentTarget);
            }

            if(ns.getServerRequiredHackingLevel(currentTarget) <= hackLvl && ns.getServerMaxMoney(currentTarget) > 0)
            {
                if(!ns.hasRootAccess(currentTarget) > 0)
                {
                    await ns.nuke(currentTarget);
                    ns.print(`Root access granted: ${currentTarget}`);
                }

                await ns.scp("grow-weaken.js", "home", currentTarget);
                ns.print(`Copied "grow-weaken.js" to ${currentTarget}`);

                let scriptRam = ns.getScriptRam("grow-weaken.js", currentTarget);
                let serverRam = ns.getServerMaxRam(currentTarget) - ns.getServerUsedRam(currentTarget);
                let maxThreads = (scriptRam > 0) ? Math.floor(serverRam / scriptRam) : 0;

                ns.print(`${currentTarget}: Max Threads = ${maxThreads}, RAM Available = ${serverRam}, Script RAM = ${scriptRam}`);

                if(maxThreads > 0)
                {
                    ns.exec("grow-weaken.js", currentTarget, maxThreads);
                    ns.print(`Executing "grow-weaken.js" on ${currentTarget} with ${maxThreads} threads`);
                }
                else
                {
                    ns.print(`Not enough RAM on ${currentTarget} to run "grow-weaken.js"!`);
                }
            } 
        }

        await ns.sleep(5000);
    }
}