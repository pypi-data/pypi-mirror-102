from ChefsHatGym.Agents import Agent_Naive_Random
from ChefsHatGym.KEF import LogManager
import csv


import gym
import numpy
import random
import math
import copy
import gc



class Tournament():


    def __init__(self, savingDirectory, verbose=True, opponentsComp=[], opponentsCoop=[], oponentsCompCoop=[],threadTimeOut=5, actionTimeOut=5,  gameType=["POINTS"], gameStopCriteria=15):
        self.savingDirectory = savingDirectory
        self.verbose= verbose
        self.threadTimeOut = threadTimeOut
        self.actionTimeout = actionTimeOut
        self.gameType = gameType
        self.gameStopCriteria = gameStopCriteria

        """Complement the group of agents to be a number pow 2"""
        self.agentsComp = self.complementGroups(opponentsComp,opponentsCoop, oponentsCompCoop)

        self.agentsCoop = opponentsCoop
        self.agentsCompCoop = oponentsCompCoop

        self.opponentsComp = [a.name for a in self.agentsComp]
        self.opponentsCoop = [a.name for a in self.agentsCoop]
        self.oponentsCompCoop = [a.name for a in self.agentsCompCoop]

    def createGroups(self):

        random.shuffle(self.agentsComp)
        random.shuffle(self.agentsCoop)
        random.shuffle(self.agentsCompCoop)

        pairs = []

        print ("Comp:" + str(len(self.agentsComp)))
        print("Coop:" + str(len(self.agentsCoop)))
        print("CompCoop:" + str(len(self.agentsCompCoop)))

        [pairs.append([self.agentsComp[i], self.agentsComp[i + 1]]) for i in list(range(len(self.agentsComp)))[::2]]
        [pairs.append([a,Agent_Naive_Random.AgentNaive_Random("TeamMate_" + str(a.name))]) for a in self.agentsCoop]
        [pairs.append([a, Agent_Naive_Random.AgentNaive_Random("TeamMate_" + str(a.name))]) for a in self.agentsCompCoop]
        random.shuffle(pairs)

        print ("Pairs:" + str(len(pairs)))
        print ("Pairs:" + str(pairs))
        groups = []
        for p in list(range(len(pairs)))[::2]:
            random.shuffle(pairs[p])
            newGroup = [pairs[p][0], pairs[p][1], pairs[p + 1][0], pairs[p + 1][1]]
            groups.append(newGroup)

        random.shuffle(groups)
        return groups


    def runTournament(self):
        """Tournament parameters"""
        saveTournamentDirectory = self.savingDirectory  # Where all the logs will be saved

        groups = self.createGroups()

        brackets = [groups[0:int(len(groups) / 2)], groups[int(len(groups) / 2):]]

        phases = int(math.log(len(brackets[0]),2))+1

        logger = LogManager.Logger(saveTournamentDirectory+"/Log.txt", verbose=True)

        names = [a.name for g in brackets[0] for a in g]

        logger.newLogSession("Tournament starting!")
        logger.write("Total players:" + str(len(self.opponentsComp) + len(self.opponentsCoop)*2 + len(self.oponentsCompCoop)*2))
        logger.write("Players COMP:" + str(len(self.opponentsComp)))
        logger.write("Players COOP:" + str(len(self.opponentsCoop)*2))
        logger.write("Players COMPCOOP:" + str(len(self.oponentsCompCoop)*2))
        logger.write("Total groups:" + str(len(groups)))
        for bIndex, b in enumerate(brackets):
            logger.write("Bracket "+str(bIndex)+":")
            for gIndex, g in enumerate(b):
                names = [a.name for a in b[gIndex]]
                logger.write(" -Group "+str(gIndex)+":"+str(names))

        logger.write("Phases per Bracket:" + str(phases))

        bWinners = []

        finalPositionComp = []
        finalPositionCoop = []
        thirds = []
        fourths = []

        outCoop = []

        for b in range(len(brackets)):
            logger.newLogSession("Starting Games from Bracket:" + str(b+1))
            thisPhaseGroup = brackets[b]
            for p in range(phases):
                logger.newLogSession("Starting Phase:" + str(p+1))
                names = [a.name for g in thisPhaseGroup for a in g]
                logger.write("- Participants:" + str(names))
                newPhaseGroups = []
                thirds.append([])
                fourths.append([])
                outCoop.append([])
                for game in range(len(thisPhaseGroup)):
                    names = [a.name for a in thisPhaseGroup[game]]
                    logger.write("- Game:" + str(game) + " - "+str(names))
                    first, second, third, fourth = self.playGame(thisPhaseGroup[game], b+1, p+1, game,saveTournamentDirectory, logger)
                    logger.write("-- First:" + str(first[0].name) + " - Second:" + str(second[0].name))

                    newPhaseGroups.append(first[0])
                    newPhaseGroups.append(second[0])

                    """Competitive Ranking"""
                    if third[0].name in self.opponentsComp or third[0].name in self.oponentsCompCoop:
                        thirds[p].append([third[0].name, third[1]])

                    if fourth[0].name in self.opponentsComp or fourth[0].name in self.oponentsCompCoop:
                        fourths[p].append([fourth[0].name, fourth[1]])

                    """Cooperative Ranking"""

                    """Find fourth's and third's team mate and log them"""
                    coopPlayers = []
                    if third[0].name in self.opponentsCoop or third[0].name in self.oponentsCompCoop:
                        coopPlayers.append(third)

                    if fourth[0].name in self.opponentsCoop or fourth[0].name in self.oponentsCompCoop:
                        coopPlayers.append(fourth)


                    for playerCoop in coopPlayers:
                        for teamMate in (first,second,third,fourth):
                            # print ("PLayer coop:" + str(playerCoop))
                            # print("TeamMate:" + str(teamMate))
                            if not playerCoop[0].name == teamMate[0].name:
                                if "TeamMate" in teamMate[0].name and playerCoop[0].name in teamMate[0].name:
                                    outCoop[p].append([[playerCoop[0].name, playerCoop[1]], [teamMate[0].name, teamMate[1]]])


                    """Check if the first and second are team mates and If not, then check which is the position of the team mate
                    """
                    if not (("TeamMate" in first[0].name and second[0].name in first[0].name) or ("TeamMate" in second[0].name and first[0].name in second[0].name)):
                        coopPlayers = []
                        if first[0].name in self.opponentsCoop or first[0].name in self.oponentsCompCoop:
                            coopPlayers.append(first)

                        if second[0].name in self.opponentsCoop or second[0].name in self.oponentsCompCoop:
                            coopPlayers.append(second)

                        for playerCoop in coopPlayers:
                            for teamMate in (first, second, third, fourth):
                                # print("PLayer coop:" + str(playerCoop))
                                # print("TeamMate:" + str(teamMate))
                                if not playerCoop[0].name == teamMate[0].name:
                                    if "TeamMate" in teamMate[0].name and playerCoop[0].name in teamMate[0].name:
                                        outCoop[p].append(
                                            [[playerCoop[0].name, playerCoop[1]], [teamMate[0].name, teamMate[1]]])

                    del third
                    del fourth
                    gc.collect()

                if p == phases-1:
                    bWinners.append(newPhaseGroups[0])
                    bWinners.append(newPhaseGroups[1])
                else:
                   thisPhaseGroup = [newPhaseGroups[g:g + 4] for g in list(range(len(newPhaseGroups)))[::4]]

                names = [a.name for a in bWinners if len(bWinners) > 0]


        """After the end of the game sort the competitive rank fourths and thirds per phase and add them the bottom of the final Position"""
        for phaseIndex in range(phases):
            fourthsThisPhase = sorted(fourths[phaseIndex], key=lambda tup: tup[1])
            [finalPositionComp.append([f[0], f[1], (phaseIndex + 1)]) for f in fourthsThisPhase]

            thirdsThisPhase = sorted(thirds[phaseIndex], key=lambda tup: tup[1])
            [finalPositionComp.append([f[0], f[1], (phaseIndex + 1)]) for f in thirdsThisPhase]

        """After the end of the game sort the cooperative agents based on the score of the teammates"""
        for phaseIndex in range(phases):
            agentsThisPhase = sorted(outCoop[phaseIndex], key=lambda tup: tup[1][1])
            [finalPositionCoop.append([f[0][0],f[0][1], f[1][0],f[1][1], (phaseIndex + 1)]) for f in agentsThisPhase]

        logger.newLogSession("Final match!")
        logger.write("- Participants:" + str(names))
        first, second, third, fourth = self.playGame(bWinners, 3, 1, 1, saveTournamentDirectory, logger)

        """After the end of the last phase add the competitive agents to the competitive rank"""
        for agent in [fourth, third, second, first]:
            if agent[0].name in self.opponentsComp or agent[0].name in self.oponentsCompCoop:
                finalPositionComp.append([agent[0].name, agent[1], phases+1])

        """After the end of the last phase add the coop agents to the cooperative rank"""
        """Find fourth's and third's team mate and log them"""
        finalCoopPositions = []
        for agent in [fourth, third, second, first]:

            if agent[0].name in self.opponentsCoop or agent[0].name in self.oponentsCompCoop:

                """Find the teammate"""
                for teamMate in (fourth, third, second, first):
                    # print ("PLayer coop:" + str(playerCoop))
                    # print("TeamMate:" + str(teamMate))
                    if not agent[0].name == teamMate[0].name:
                        if "TeamMate" in teamMate[0].name and agent[0].name in teamMate[0].name:
                            finalCoopPositions.append(
                                [[agent[0].name, agent[1]], [teamMate[0].name, teamMate[1]]])


        agentsThisPhase = sorted(finalCoopPositions, key=lambda tup: tup[1][1])
        [finalPositionCoop.append([f[0][0], f[0][1], f[1][0], f[1][1], (phases + 1)]) for f in agentsThisPhase]


        logger.write("-- Final position:")
        logger.write("-- 1)" + str(first[0].name))
        logger.write("-- 2)" + str(second[0].name))
        logger.write("-- 3)" + str(third[0].name))
        logger.write("-- 4)" + str(fourth[0].name))

        """Writing comp rank"""
        with open(self.savingDirectory+"/FinalResultsComp.csv", mode='w') as csvFile:
            csvWriter = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            csvWriter.writerow(["Position", 'Player Name', 'Final Game Performance Score', 'Games Played'])
            for pIndex, player in enumerate(reversed(finalPositionComp)):
                csvWriter.writerow([(pIndex+1), player[0], player[1], player[2]])


        """Writing coop rank"""
        with open(self.savingDirectory+"/FinalResultsCoop.csv", mode='w') as csvFile:
            csvWriter = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            csvWriter.writerow(["Position", 'Player Name', 'Final Game Performance Score',  "TeamMate Name", "TeamMate Final Game Performance Score" ,'Games Played Team Mate'])
            for pIndex, player in enumerate(reversed(finalPositionCoop)):
                csvWriter.writerow([(pIndex+1), player[0], player[1], player[2], player[3],player[4]])


    """Get Random action"""
    def getRandomAction(self, possibleActions):
        itemindex = numpy.array(numpy.where(numpy.array(possibleActions) == 1))[0].tolist()

        random.shuffle(itemindex)
        aIndex = itemindex[0]
        a = numpy.zeros(200)
        a[aIndex] = 1

        return a

    """Complement the opponents with random agents until we have enough to create two brackets"""
    def complementGroups(self, comp, coop, compCoop):


        totalAgents = len(comp) + len(coop)*2 + len(compCoop)*2
        # print ("Total agents:" + str(totalAgents))

        difference = float(math.log(totalAgents,2))
        # print("Difference:" + str(difference))
        group = []
        [group.append(a) for a in comp]

        if difference.is_integer():
            if totalAgents < 8:
                for n in range(int(8-totalAgents)):
                    group.append(Agent_Naive_Random.AgentNaive_Random("RandomGYM_" + str(n)))

            return group
        else:
            intDiff = math.modf(difference)[1]

            newAdditions = int(math.pow(2,intDiff+1) - totalAgents)

            for n in range(newAdditions):
                group.append(Agent_Naive_Random.AgentNaive_Random("RandomGYM_"+str(n)))

        return group


    """Playing a Game"""
    def playGame(self, group, bracket, round, gameNumber, saveDirectory, logger):

        """Experiment parameters"""
        saveDirectory = saveDirectory+"/Bracket_"+str(bracket)+"/Phase_"+str(round)+"/Game_"+str(gameNumber)
        verbose = False
        saveLog = True
        saveDataset = True

        agentNames = [agent.name for agent in group]

        rewards = []
        for agent in group:
            rewards.append(agent.getReward)

        """Setup environment"""
        env = gym.make('chefshat-v0') #starting the game Environment
        env.startExperiment(rewardFunctions=rewards, gameType=self.gameType, stopCriteria=self.gameStopCriteria, playerNames=agentNames, logDirectory=saveDirectory, verbose=verbose, saveDataset=saveDataset, saveLog=saveLog)

        observations = env.reset()

        while not env.gameFinished:
            currentPlayer = group[env.currentPlayer]

            observations = env.getObservation()

            action = []
            with currentPlayer.timeout(self.actionTimeout):
                action = currentPlayer.getAction(observations)
            if len(action) == 0:
                action = self.getRandomAction(observations[28:])

            info = {"validAction": False}
            while not info["validAction"]:
                nextobs, reward, isMatchOver, info = env.step(action)

            # Training will be called in a thread, that will be killed inself.threadTimes
            # self.runUpdateAction(currentPlayer, args=(observations, nextobs, action, reward, info) )
            with currentPlayer.timeout(self.threadTimeOut):
                currentPlayer.actionUpdate(observations, nextobs, action, reward, info)

            # self.startThread(currentPlayer.actionUpdate, args=(observations, nextobs, action, reward, info))
            # currentPlayer.actionUpdate(observations, nextobs, action, reward, info)


            # Observe others
            for p in group:
                # Observe Others will be called in a thread, that will be killed in self.threadTimes
                with p.timeout(self.threadTimeOut):
                    p.observeOthers(info)
            #
            if isMatchOver:
                # Update the match info as a thread that will be killed in self.threadTimes
                for p in group:
                    with p.timeout(self.threadTimeOut):
                        p.matchUpdate(info)




        sortedScore = copy.copy(info["score"])
        sortedScore.sort()

        winnerIndex = info["score"].index(sortedScore[-1])
        performanceScoreWinner = info["performanceScore"][winnerIndex]

        secondIndex = info["score"].index(sortedScore[-2])
        performanceScoreSecond = info["performanceScore"][secondIndex]

        thirdIndex = info["score"].index(sortedScore[-3])
        performanceScoreThird = info["performanceScore"][thirdIndex]

        fourthIndex = info["score"].index(sortedScore[-4])
        performanceScoreFourth = info["performanceScore"][fourthIndex]

        winner = group[winnerIndex]
        second = group[secondIndex]
        third = group[thirdIndex]
        fourth = group[fourthIndex]

        if self.verbose:
            logger.write("-- Performance:" + str(info["performanceScore"]))
            logger.write("-- Points:" + str(info["score"]))

        return [winner,performanceScoreWinner], [second, performanceScoreSecond], [third,performanceScoreThird], [fourth,performanceScoreFourth]






