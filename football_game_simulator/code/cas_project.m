% Define parameters

%pyenv("Version",'./Library/Frameworks/Python.framework/Versions/3.10')

MDP = createMDP(12,["doNothing";"improve_1";"improve_2"]);

%pyrunfile("main.py", "team1_total")
% Win and loss values
win_values = [0.2233, 0.2558, 0.3180];
loss_values = [1 - 0.2233, 1 - 0.2558, 1 - 0.3180];

% Define states for MDP
states = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
actions = [1, 2, 3];
indexing = 1;
loop_states = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];

% Loop through each state and action to populate transition and reward matrices
for state = loop_states
    if state == 2 || state == 3
        indexing = 1;
    elseif state == 5 || state == 6 || state == 7
        indexing = 2;
    elseif state == 9 || state == 10 || state == 11
        indexing = 3;
    end
    for action = actions
        if mod(state,4) == 0 
            % Terminal state, set transition probability to 1 and reward to 0
            MDP.T(state, state, action) = 1;
            MDP.R(state, state, action) = 15;
        else
            % Non-terminal states
            if action == 1 
                % Action 1 transitions or state 1 
                MDP.T(state, [state, state+1], action) = [loss_values(indexing), win_values(indexing)];
                MDP.R(state, state, action) = 0;
                MDP.R(state, state+1, action) = 5;
            else
                % Actions 2 and 3 transitions
                MDP.T(state, state, action) = 1;
                MDP.R(state, state, action) = -5;
            end
        end
    end
end

MDP.T(1,[1,2],1) = [loss_values(1) win_values(1)];
MDP.R(1,1,1) = -1;
MDP.R(1,2,1) = 1;
MDP.T(1,[4,5],2) = [loss_values(2) win_values(2)];
MDP.R(1,4,2) = -1;
MDP.R(1,5,2) = 2;
MDP.T(1,[7,8],3) = [loss_values(3) win_values(3)];
MDP.R(1,7,3) = -1;
MDP.R(1,8,3) = 3;

MDP.TerminalStates = ["s4";"s8";"s12"];

env = rlMDPEnv(MDP);

env.ResetFcn = @() 1;

obsInfo = getObservationInfo(env);
actInfo = getActionInfo(env);
qTable = rlTable(obsInfo, actInfo);
qFunction = rlQValueFunction(qTable, obsInfo, actInfo);
qOptions = rlOptimizerOptions(LearnRate=1);

agentOpts = rlQAgentOptions;
agentOpts.DiscountFactor = 1;
agentOpts.EpsilonGreedyExploration.Epsilon = 0.9;
agentOpts.EpsilonGreedyExploration.EpsilonDecay = 0.1;
agentOpts.CriticOptimizerOptions = qOptions;
qAgent = rlQAgent(qFunction,agentOpts); 

trainOpts = rlTrainingOptions;
trainOpts.MaxStepsPerEpisode = 500;
trainOpts.MaxEpisodes = 50;
trainOpts.StopTrainingCriteria = "AverageReward";
trainOpts.StopTrainingValue = 10;
trainOpts.ScoreAveragingWindowLength = 100;

trainingStats = train(qAgent,env,trainOpts);





