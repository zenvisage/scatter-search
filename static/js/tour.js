var tour = {
    id: "hello-hopscotch",
    steps: [
        {
            target: "title",
            title: "Welcome to Scatter Search",
            content: "Although the documentation is fairly elaborate, let's quickly go through how the app works",
            placement: "bottom",
            xOffset: 'center',
            arrowOffset: 'center'
        },
        {
            target: "help",
            title: "This tutorial is here to stay",
            content: "You can always watch the tutorial again by clicking on this button.",
            placement: "left"
        },
        {
            target: "main-chart",
            placement: "bottom",
            title: "Your Playground",
            content: "This plot represents the overall dataset based on the settings on the left. " +
            "It is where you'll interact the most in and specify areas of exploration."
        },
        {
            target: "dataset-settings",
            placement: "right",
            title: "Decide your perspective",
            content: "Use these settings to update the view and perspective of the representative plot!"
        },
        {
            target: "update-dataset-settings",
            placement: "right",
            title: "Update View",
            content: "Hit Update to affect the Representative Plot."
        },
        {
            target: "algorithm",
            placement: "right",
            title: "Choose your weapon",
            content: "Here are all the algorithms implemented in the system currently. Choose wisely. Their descriptions should appear alongside the results."
        },
         {
            target: "drawing",
            placement: "left",
            title: "Tools for drawing",
            content: "These are explained in detail in the green box below."
        },
        {
            target: "get-results",
            placement: "top",
            title: "Results.",
            content: "And ofcourse, hit this button to get the results on a different page.",
        },
        {
            target: "title",
            placement: "bottom",
            title: "You're all set!",
            content: "Good luck with your exploration!",
            xOffset: 'center',
            arrowOffset: 'center'
        }
    ],
    showPrevButton: true,
    scrollTopMargin: 100
};